# Generated by Django 4.2.2 on 2023-08-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_record_date_job_start_date_alter_job_casing_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
