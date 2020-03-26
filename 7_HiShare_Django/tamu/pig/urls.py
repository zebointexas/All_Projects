from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls import include

app_name = 'pig'

urlpatterns = [


     ########################################################################################
     # Have a Ride
     url(r'^ride$', views.RideView.as_view(), name='ride'),
     # Details
     url(r'^(?P<pk>[0-9]+)/ride$', views.RideDetailView.as_view(), name='ride-detail'),
     # Add a Ride
     url(r'ride/add/$', views.AddRide.as_view(), name='ride-add'),
     ########################################################################################

     ########################################################################################
     # Ask for a Ride
     url(r'^ask-ride$', views.AskRideView.as_view(), name='ask-ride'),
     # Details
     url(r'^(?P<pk>[0-9]+)/ask-ride$', views.AskRideDetailView.as_view(), name='ask-ride-detail'),
     # Add a Ride
     url(r'ask-ride-ask/add/$', views.AddAskRide.as_view(), name='ask-ride-add'),
     ########################################################################################



     url(r'^', views.IndexView.as_view(), name='index'),  # /pig/

     url(r'^register/$', views.UserFormView.as_view(), name='register'),

     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),  # /music/<album_id>/

     url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

     url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

     url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]


