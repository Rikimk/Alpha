from typing import List
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Album, Artist, Language, Genre

# Create your views here.

def index(request):
    num_of_albums = Album.objects.all().count()
    num_of_artists = Artist.objects.all().count()

    context = {
        'num_of_albums':num_of_albums,
        'num_of_artists':num_of_artists,
    }

    return render(request,'catalogue/index.html',context=context)

class AlbumListView(ListView):
    model = Album
    queryset = Album.objects.order_by('name')
    context_object_name = 'album_list'

class AlbumDetail(DetailView):
    model = Album