# Generated by Django 2.0 on 2019-01-10 19:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0019_auto_20190110_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='depart_date',
            field=models.DateTimeField(default='1997-07-01'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 10, 19, 22, 44, 255089, tzinfo=utc)),
        ),
    ]