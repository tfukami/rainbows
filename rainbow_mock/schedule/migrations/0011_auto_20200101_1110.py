# Generated by Django 3.0 on 2020-01-01 02:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_auto_20200101_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 1, 2, 10, 18, 523306, tzinfo=utc), verbose_name='日付'),
        ),
    ]
