# Generated by Django 3.0 on 2020-01-07 11:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0020_auto_20200106_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 7, 11, 56, 45, 364488, tzinfo=utc), verbose_name='日付'),
        ),
    ]
