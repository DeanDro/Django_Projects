# Generated by Django 3.2.5 on 2021-09-07 04:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20210906_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profiles',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='deadline',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='description',
            field=models.CharField(default='whatever project', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='members',
            field=models.CharField(default='team', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='name',
            field=models.CharField(default='admin', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='owner',
            field=models.CharField(default='secretary', max_length=50),
            preserve_default=False,
        ),
    ]