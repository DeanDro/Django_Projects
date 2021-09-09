# Generated by Django 3.2.5 on 2021-09-07 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20210907_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='name',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='username',
        ),
        migrations.RemoveField(
            model_name='projectdata',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='projectdata',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projectdata',
            name='members',
        ),
        migrations.RemoveField(
            model_name='projectdata',
            name='name',
        ),
        migrations.RemoveField(
            model_name='projectdata',
            name='owner',
        ),
        migrations.AddField(
            model_name='profiles',
            name='profile_name',
            field=models.CharField(default='admin', max_length=40),
        ),
        migrations.AddField(
            model_name='projectdata',
            name='project_name',
            field=models.CharField(default='New Meeting', max_length=40),
        ),
    ]