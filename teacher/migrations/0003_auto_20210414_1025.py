# Generated by Django 3.0.7 on 2021-04-14 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_remove_addressinfo_village'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobinfo',
            name='department',
        ),
        migrations.RemoveField(
            model_name='jobinfo',
            name='job_designation',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='education',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='job',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='training',
        ),
        migrations.DeleteModel(
            name='EducationInfo',
        ),
        migrations.DeleteModel(
            name='ExperienceInfo',
        ),
        migrations.DeleteModel(
            name='JobInfo',
        ),
        migrations.DeleteModel(
            name='TrainingInfo',
        ),
    ]
