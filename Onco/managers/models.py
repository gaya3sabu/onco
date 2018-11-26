from django.db import models
CHOICES1 = (('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender'))
CHOICES3 = (('Kasargod', 'Kasargod'), ('Kannur', 'Kannur'), ('Wayanad', 'Wayanad'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Thrissur', 'Thrissur'),
('Ernakulam', 'Ernakulam'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Pathanamthitta', 'Pathanamthitta'), ('Kollam', 'Kollam'), ('Thiruvanathapuram', 'Thiruvanathapuram'),
            ('Palakkad', 'Palakkad'))



class Managers(models.Model):
    mgr_name = models.CharField(max_length=30, default='')
    mgr_gender = models.CharField(max_length=30, choices=CHOICES1)
    mgr_age = models.BigIntegerField()
    mgr_place = models.CharField(max_length=30, default='')
    mgr_city = models.CharField(max_length=30, default='')
    mgr_district = models.CharField(max_length=30, choices=CHOICES3)
    mgr_phone = models.CharField(max_length=30, default='')
    mgr_email = models.EmailField(max_length=30, default='')
    mgr_username = models.CharField(max_length=30, default='')
    mgr_password = models.CharField(max_length=30, default='')




def __str__(self):
    return self.name

