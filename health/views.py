from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HealthSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
class PredictObesity(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Step 1: Load the dataset
        dataset = pd.read_csv("C:\\Users\\EBM\\OneDrive\\Bureau\\Check_Your_health\\server\\health\\ObesityDataSet.csv")

        # Step 2: Define mapping
        mapping = {
            "Gender": {"Female": 2, "Male": 1},
            "family_history_with_overweight": {"yes": 1, "no": 0},
            "FAVC": {"yes": 1, "no": 0},
            "CAEC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3},
            "FCVC": {"no": 0, "Sometimes": 1, "Frequently": 2},
            "SMOKE": {"yes": 1, "no": 0},
            "SCC": {"yes": 1, "no": 0},
            "CALC": {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3},
            "MTRANS": {"Automobile": 1, "Motorbike": 2, "Public_Transportation": 3, "Walking": 4, "Bike": 5},
            "NObeyesdad": {"Normal_Weight": 1, "Overweight_Level_I": 2, "Overweight_Level_II": 3,
                           "Obesity_Type_I": 4, "Obesity_Type_II": 5, "Obesity_Type_III": 6, "Insufficient_Weight": 7}
        }
        dataset.replace(mapping,inplace=True)


        # Step 3: Extract input data from the request
        input_data = request.data
        print(input_data)
        # Step 4: Define the encode_input function
        def encode_input(data, mapping):
            encoded_data = {}
            for key, value in data.items():

                if key in mapping:
                    encoded_data[key] = mapping[key][value] if value in mapping[key] else value

                else:
                    encoded_data[key] = value

            return encoded_data

        # Step 5: Encode the input data
        encoded_input = encode_input(input_data, mapping)

        # Step 6: Convert encoded input into a DataFrame
        new_data_df = pd.DataFrame([encoded_input])

        # Step 7: Load the trained model
        classifier = RandomForestClassifier()
        X = dataset.iloc[:, :-1]  # Features
        y = dataset.iloc[:, -1]   # Target
        classifier.fit(X, y)

        # Step 8: Predict the class of NObeyesdad for the new data using the trained classifier
        predicted_class = classifier.predict(new_data_df)

        # Step 9: Map the predicted class back to its original label
        predicted_class_label = list(mapping['NObeyesdad'].keys())[predicted_class[0] - 1]
    
        # Step 10: Return the predicted class label in the response
        return Response({'predicted_class': predicted_class_label})



