# Generated by Django 2.0 on 2019-01-03 05:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pig', '0003_album_ride_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file_type',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
