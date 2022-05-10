from typing import List
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from .forms import CreateUserForm
from .models import Album, Artist, Language, Genre
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .decorators import unauthenticated_user

# Create your views here.

def homePage(request):
    return render(request, 'home.html')

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

@login_required(login_url='login')
def my_view(request):
    return render(request, 'catalogue/my_view.html')

@unauthenticated_user
def registerPage(request):
   
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'registration/register.html', context)

@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('catalogue:index')
        else:
            messages.info(request, 'Username or Password incorrect!')
    context = {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')