# Generated by Django 2.1.1 on 2018-10-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bduser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Transgender', 'Transgender')], max_length=30)),
                ('age', models.BigIntegerField()),
                ('place', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('district', models.CharField(choices=[('Kasargod', 'Kasargod'), ('Kannur', 'Kannur'), ('Wayanad', 'Wayanad'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Thrissur', 'Thrissur'), ('Ernakulam', 'Ernakulam'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Pathanamthitta', 'Pathanamthitta'), ('Kollam', 'Kollam'), ('Thiruvanathapuram', 'Thiruvanathapuram'), ('Palakkad', 'Palakkad')], max_length=30)),
                ('phone', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('bloodgroup', models.CharField(choices=[('A+ve', 'A+ve'), ('B+ve', 'B+ve'), ('O+ve', 'O+ve'), ('AB+ve', 'AB+ve'), ('A-ve', 'A-ve'), ('B-ve', 'B-ve'), ('AB-ve', 'AB-ve'), ('O-ve', 'O-ve')], max_length=30)),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
