# Generated by Django 2.1.1 on 2018-10-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20181021_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.CharField(default='', max_length=30),
        ),
    ]
