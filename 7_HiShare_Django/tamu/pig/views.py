from audioop import reverse

from django.views import generic
from .models import Album, Ride, AskRide
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

##################################################################
# Ride
class RideView(generic.ListView):
    template_name = 'pig/ride.html'
    context_object_name = 'all_rides'

    def get_queryset(self):
        return Ride.objects.all().order_by ('-Depart_Date')

class RideDetailView(generic.DetailView):
    model = Ride
    template_name = 'pig/ride_detail.html'

class AddRide(CreateView):
    model = Ride
    fields = ['Depart_Date', 'From', 'To', 'Total_Seats_Available', 'Mobile', 'WeChat','Student_Or_Not', 'Gas_Need']
##################################################################


##################################################################
# Ask Ride
class AskRideView(generic.ListView):
    template_name = 'pig/ask-ride.html'
    context_object_name = 'all_requests'

    def get_queryset(self):
        return AskRide.objects.all().order_by ('-Depart_Date')

class AskRideDetailView(generic.DetailView):
    model = AskRide
    template_name = 'pig/ask-ride_detail.html'

class AddAskRide(CreateView):
    model = AskRide
    fields = ['Depart_Date', 'From', 'To', 'Seats_Needed', 'Mobile', 'WeChat','Student_Or_Not', 'Gas_Return']
##################################################################


class IndexView(generic.ListView):
    template_name = 'pig/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album;
    template_name = 'pig/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('pig:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'pig/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('pig:index')

        return render(request, self.template_name, {'form':form})































# from django.http import Http404
# from django.http import HttpResponse
# from .models import Album, Song
# from django.template import loader
# from django.shortcuts import render, get_object_or_404

#def index(request):
#    all_albums = Album.objects.all()
#    context = {'all_albums':all_albums}
#    return render(request, 'pig/index.html', context)

#	def index(request):
#    all_albums = Album.objects.all()
#    template = loader.get_template('pig/index.html')
#    context = {
#        'all_albums': all_albums,
#    }
#    return HttpResponse(template.render(context, request))

#	def index(request):
#    all_albums = Album.objects.all();
#    html = ''
#    for album in all_albums:
#        url = '/pig/' + str(album.id) + '/'
#        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
#    return HttpResponse(html)

#def detail(request, album_id):
    #    try:
    #        album = Album.objects.get(pk=album_id)
    #    except Album.DoesNotExist:
    #        raise Http404("<h1>Sorry it is Jin Liuyi's fault</h1>")
#    return render(request, 'pig/detail.html', {'album':album})

#def detail(request, album_id):
    #    album = get_object_or_404(Album, pk=album_id)
#    return render(request, 'pig/detail.html', {'album': album})

#def favorite(request, album_id):
    #    album = get_object_or_404(Album, pk=album_id)

    #    try:
    #        selected_song = album.song_set.get(pk=request.POST['song'])
    #    except (KeyError, Song.DoesNotExist):
    #        return render(request, 'pig/detail.html', {
    #           'album': album,
    #           'error_message': "You did not select a valid song",
    #      })
    #   else:
    #        selected_song.is_favorite = True
    #        selected_song.save()
#        return render(request, 'pig/detail.html', {'album':album})




