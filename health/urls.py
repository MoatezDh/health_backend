from django.urls import path
from .views import HealthListCreateAPIView, PredictObesity

urlpatterns = [
    path('api/health/', HealthListCreateAPIView.as_view(), name='health-list-create'),
    path('api/predict', PredictObesity.as_view(), name='health-list-predict'),
    
]
