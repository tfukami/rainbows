# Generated by Django 3.0 on 2020-01-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200106_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.IntegerField(choices=[(0, '男性'), (1, '女性')], max_length=3, null=True, verbose_name='性別'),
        ),
    ]
