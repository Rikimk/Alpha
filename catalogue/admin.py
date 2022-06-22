from django.contrib import admin
from .models import Album, Artist, Language, Genre, Band, Profile, Role, Review
# Register your models here.

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Review)