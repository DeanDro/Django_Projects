# Generated by Django 3.2.5 on 2021-09-09 04:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='admin_user', max_length=50)),
                ('name', models.CharField(default='admin', max_length=50)),
                ('email', models.CharField(default='admin@admin_mail.com', max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='projectdata',
            name='deadline',
            field=models.CharField(default='12/12/2021', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdata',
            name='members_list',
            field=models.CharField(default='myself', max_length=150),
        ),
        migrations.AddField(
            model_name='projectdata',
            name='project_description',
            field=models.CharField(default='Setup the team meeting for next week', max_length=150),
        ),
        migrations.AddField(
            model_name='projectdata',
            name='project_owner',
            field=models.CharField(default='K', max_length=100),
        ),
        migrations.AddField(
            model_name='projectdata',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectdata',
            name='project_name',
            field=models.CharField(default='Next Meeting', max_length=100),
        ),
    ]