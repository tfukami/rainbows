# Generated by Django 3.0 on 2020-01-05 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0017_auto_20200105_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 5, 8, 4, 48, 208775, tzinfo=utc), verbose_name='日付'),
        ),
    ]
