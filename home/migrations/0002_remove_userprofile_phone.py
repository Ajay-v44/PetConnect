# Generated by Django 5.1.1 on 2024-10-06 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
    ]
