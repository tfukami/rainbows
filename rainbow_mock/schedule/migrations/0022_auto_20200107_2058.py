# Generated by Django 3.0 on 2020-01-07 11:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_auto_20200107_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 7, 11, 58, 8, 374293, tzinfo=utc), verbose_name='日付'),
        ),
    ]
