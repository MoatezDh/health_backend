from django.urls import path
from .views import PredictObesity

urlpatterns = [
    path('api/predict', PredictObesity.as_view(), name='predict-obesity'),
]
