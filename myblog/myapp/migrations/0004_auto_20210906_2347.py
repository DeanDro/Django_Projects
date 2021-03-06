# Generated by Django 3.2.5 on 2021-09-07 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210906_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdata',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='projectdata',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='members',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='owner',
            field=models.CharField(max_length=50),
        ),
    ]
