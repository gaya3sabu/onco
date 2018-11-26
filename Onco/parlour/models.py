from django.db import models
from managers .models import Managers
CHOICES = (('Kasargod', 'Kasargod'), ('Kannur', 'Kannur'), ('Wayanad', 'Wayanad'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Thrissur', 'Thrissur'),
('Ernakulam', 'Ernakulam'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Pathanamthitta', 'Pathanamthitta'), ('Kollam', 'Kollam'), ('Thiruvanathapuram', 'Thiruvanathapuram'),
            ('Palakkad', 'Palakkad'))

class Parlour(models.Model):
    parlour_id = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='')
    place = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=30, choices=CHOICES)
    email = models.CharField(max_length=30, default='')
    phone = models.CharField(max_length=30, default='')
    mgr_id = models.BigIntegerField()


    def __str__(self):
        return self.name

