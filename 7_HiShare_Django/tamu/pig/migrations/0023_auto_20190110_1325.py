# Generated by Django 2.0 on 2019-01-10 19:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0022_auto_20190110_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 19, 25, 59, 473967, tzinfo=utc)),
        ),
    ]
