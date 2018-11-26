from django.db import models
from managers .models import Managers


class Cancerdet(models.Model):
    name = models.CharField(max_length=50, default='')
    symptom = models.CharField(max_length=50, default='')
    cause = models.CharField(max_length=50, default='')
    test = models.CharField(max_length=50, default='')
    treatment = models.CharField(max_length=50, default='')
    mgr_id = models.BigIntegerField()

    def __str__(self):
        return self.name
