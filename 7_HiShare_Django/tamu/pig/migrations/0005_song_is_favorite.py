# Generated by Django 2.0 on 2019-01-04 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0004_auto_20190102_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
