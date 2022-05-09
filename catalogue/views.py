from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from .models import Album, Artist, Language, Genre
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    num_of_albums = Album.objects.all().count()
    num_of_artists = Artist.objects.all().count()

    context = {
        'num_of_albums':num_of_albums,
        'num_of_artists':num_of_artists,
    }

    return render(request,'catalogue/index.html',context=context)

class AlbumCreate(LoginRequiredMixin,CreateView):
    model = Album
    fields = '__all__'

class AlbumListView(ListView):
    model = Album
    queryset = Album.objects.order_by('name')
    context_object_name = 'album_list'

class AlbumDetail(DetailView):
    model = Album

@login_required
def my_view(request):
    return render(request, 'catalogue/my_view.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalogue/signup.html'