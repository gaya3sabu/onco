# Generated by Django 2.1.1 on 2018-09-21 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('place', models.CharField(default='', max_length=30)),
                ('city', models.CharField(default='', max_length=30)),
                ('district', models.CharField(default='', max_length=30)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.CharField(default='', max_length=30)),
                ('hosp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
            ],
        ),
    ]