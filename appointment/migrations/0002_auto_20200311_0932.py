# Generated by Django 3.0.3 on 2020-03-11 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
