from django.db import models

class Charity(models.Model):
    charitytype = models.CharField(max_length=30, default='')


    def __str__(self):
        return self.charitytype

