# Generated by Django 2.1.1 on 2018-09-21 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('gender', models.CharField(default='', max_length=30)),
                ('age', models.CharField(default='', max_length=30)),
                ('place', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('district', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('bloodgroup', models.CharField(default='', max_length=30)),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('charitytype', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
