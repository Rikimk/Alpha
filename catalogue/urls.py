from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('',views.index,name='index'),
    path('album_detail/<int:pk>',views.AlbumDetail.as_view(),name='album_detail'),
    path('list_album',views.AlbumListView.as_view(),name='list_album'),
]
