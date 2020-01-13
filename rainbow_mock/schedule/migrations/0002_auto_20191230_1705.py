# Generated by Django 3.0 on 2019-12-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='パートナーの名前'),
        ),
        migrations.AddField(
            model_name='prof',
            name='nick_name',
            field=models.CharField(default='jack/peter/mike/etc..', max_length=100, verbose_name='ニックネーム'),
        ),
        migrations.AlterField(
            model_name='children',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='子供の名前'),
        ),
    ]
