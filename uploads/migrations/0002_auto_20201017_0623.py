# Generated by Django 2.2.13 on 2020-10-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
