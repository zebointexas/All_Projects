# Generated by Django 2.0 on 2019-02-06 05:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0028_auto_20190203_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='From_City',
            field=models.CharField(default='College Station', max_length=200),
        ),
        migrations.AddField(
            model_name='ride',
            name='To_City',
            field=models.CharField(default='Houston', max_length=200),
        ),
        migrations.AlterField(
            model_name='ride',
            name='Add_Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 6, 5, 32, 2, 836285, tzinfo=utc)),
        ),
    ]
