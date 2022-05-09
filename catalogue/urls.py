from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('',views.index,name='index'),
    path('create_album',views.AlbumCreate.as_view(),name='album_create'),
    path('album_detail/<int:pk>',views.AlbumDetail.as_view(),name='album_detail'),
    path('list_album',views.AlbumListView.as_view(),name='list_album'),
    path('my_view',views.my_view,name='my_view'),
    path('signup/',views.SignUp.as_view(),name='signup'),
]
