from email.policy import default
from tkinter import E
from unicodedata import name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id = User.pk
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=50,default='John')
    last_name = models.CharField(max_length=50,default='Doe')
    website = models.CharField(max_length=50,default='None')
    github = models.CharField(max_length=50,default='None')
    twitter = models.CharField(max_length=50,default='None')
    instagram = models.CharField(max_length=50,default='None')
    facebook = models.CharField(max_length=50,default='None')
    address = models.CharField(max_length=50,default='None')


    def __str__(self):
        return self.user.username

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100,blank=True,null=True)
    role = models.ManyToManyField(Role)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(blank=True,null=True)
    image = models.ImageField(default='default.jpg', upload_to='artist_pics')


    def get_absolute_url(self):
        return reverse("artist_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Band(models.Model):
    name = models.CharField(max_length=100)
    date_formed = models.DateField()
    members = models.ManyToManyField(Artist)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(default='default.jpg', upload_to='band_pics')

    def get_absolute_url(self):
        return reverse("band_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name
    


class Album(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey('Artist',on_delete=models.RESTRICT,null=True,blank=True)
    band = models.ForeignKey('Band',on_delete=models.RESTRICT,null=True,blank=True)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()
    language = models.ForeignKey('Language',on_delete=models.RESTRICT)
    num_of_songs = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default='default.jpg', upload_to='album_pics')

    def __str__(self):
        return f'{self.name} by {self.author or self.band}'

    def get_absolute_url(self):
        return reverse("album_detail", kwargs={"pk": self.pk})

    

    
