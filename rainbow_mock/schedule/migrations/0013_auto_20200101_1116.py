# Generated by Django 3.0 on 2020-01-01 02:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0012_auto_20200101_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 1, 2, 16, 9, 992030, tzinfo=utc), verbose_name='日付'),
        ),
    ]