from django.db import models

class Charityorg(models.Model):
    name = models.CharField(max_length=30, default='')
    place = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=30, default='')
    email = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=30, default='')
    charitytype = models.CharField(max_length=30, default='')
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=30, default='')



    def __str__(self):
        return self.name

