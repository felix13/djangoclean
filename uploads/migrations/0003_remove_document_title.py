# Generated by Django 2.2.13 on 2020-10-17 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20201017_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]
