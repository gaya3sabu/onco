# Generated by Django 2.1.1 on 2018-11-19 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0005_hospital_hosp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='hosp_id',
            field=models.CharField(default='', max_length=30),
        ),
    ]