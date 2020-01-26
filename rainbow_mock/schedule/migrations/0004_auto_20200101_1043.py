# Generated by Django 3.0 on 2020-01-01 01:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20200101_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='period',
            field=models.IntegerField(choices=[(0, '午前'), (1, '正午'), (2, '午後')], default=0, max_length=2, verbose_name='時間帯'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='schedule_date',
            field=models.DateField(default=datetime.datetime(2020, 1, 1, 1, 43, 50, 27012, tzinfo=utc), verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.IntegerField(choices=[(0, '●'), (1, '▲'), (2, '×')], default=1, max_length=1, verbose_name='状態'),
        ),
    ]