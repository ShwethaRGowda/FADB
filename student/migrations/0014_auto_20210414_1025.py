# Generated by Django 3.0.7 on 2021-04-14 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20210414_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=395860, unique=True),
        ),
    ]
