# Generated by Django 3.2.16 on 2022-11-22 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0016_auto_20221122_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbalance',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
