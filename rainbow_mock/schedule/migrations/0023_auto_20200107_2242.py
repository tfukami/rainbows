# Generated by Django 3.0 on 2020-01-07 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0022_auto_20200107_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 7, 13, 42, 29, 110213, tzinfo=utc), verbose_name='日付'),
        ),
    ]
