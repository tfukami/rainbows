# Generated by Django 3.0 on 2020-01-06 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0019_auto_20200105_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 6, 13, 30, 21, 100671, tzinfo=utc), verbose_name='日付'),
        ),
    ]
