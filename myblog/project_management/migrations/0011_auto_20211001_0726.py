# Generated by Django 3.2.5 on 2021-10-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0010_auto_20211001_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdata',
            name='deadline',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
