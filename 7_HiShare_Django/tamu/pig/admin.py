from django.contrib import admin
from .models import Album, Song, Ride, AskRide

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Ride)
admin.site.register(AskRide)