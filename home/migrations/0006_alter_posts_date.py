# Generated by Django 5.1.1 on 2024-10-06 14:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
