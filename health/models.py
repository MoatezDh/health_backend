from django.db import models
from django.contrib.auth.models import User

class Health(models.Model):
    user_name=models.CharField(max_length=50, null=True, blank=True)
    user_Age = models.IntegerField(null=True, blank=True)
    user_Height = models.FloatField(null=True, blank=True)
    user_Weight = models.FloatField(null=True, blank=True)
    family_history_with_overweight = models.BooleanField(default=False)
    FAVC = models.BooleanField(default=False)
    FCVC = models.FloatField(null=True, blank=True)
    SCC = models.BooleanField(default=False)
    FAF = models.FloatField(null=True, blank=True)
    TUE = models.FloatField(null=True, blank=True)
    NCP = models.IntegerField(null=True, blank=True)
    CAEC = models.CharField(max_length=50, null=True, blank=True)
    Smoke = models.BooleanField(default=False)
    CH2O = models.FloatField(null=True, blank=True)
    CALC = models.CharField(max_length=50, null=True, blank=True)
    Transportation = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.user_name
