# Generated by Django 3.0.3 on 2020-03-23 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20200323_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='timer',
            field=models.CharField(max_length=25),
        ),
    ]
