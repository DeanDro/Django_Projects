# Generated by Django 3.2.5 on 2021-09-29 20:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0005_meetings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetings',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 29, 16, 44, 37, 563607)),
        ),
    ]
