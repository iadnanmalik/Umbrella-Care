# Generated by Django 3.0.3 on 2020-03-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_auto_20200311_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.CharField(default='none', max_length=25),
        ),
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='none@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
