from django.db import models
CHOICES1 = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
CHOICES2 = (('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('O+ve', 'O+ve'), ('AB+ve', 'AB+ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'),  ('AB-ve', 'AB-ve'), ('O-ve', 'O-ve'))
CHOICES3 = (('Kasargod', 'Kasargod'), ('Kannur', 'Kannur'), ('Wayanad', 'Wayanad'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Thrissur', 'Thrissur'),
('Ernakulam', 'Ernakulam'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Pathanamthitta', 'Pathanamthitta'), ('Kollam', 'Kollam'), ('Thiruvanathapuram', 'Thiruvanathapuram'),
            ('Palakkad', 'Palakkad'))


class User(models.Model):
    name = models.CharField(max_length=30, default='')
    gender = models.CharField(max_length=30, choices=CHOICES1)
    age = models.BigIntegerField()
    place = models.CharField(max_length=30, default='')
    city = models.CharField(max_length=30, default='')
    district = models.CharField(max_length=30, choices=CHOICES3)
    phone = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=30, default='')
    username = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=30, default='')


def __str__(self):
    return self.name
