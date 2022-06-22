from django.urls import path
from . import views

app_name = 'catalogue'

urlpatterns = [
    path('',views.index,name='index'),
    path('create_album_artist',views.AlbumCreateArtist.as_view(),name='album_create_artist'),
    path('create_album_band',views.AlbumCreateBand.as_view(),name='album_create_band'),
    path('album_detail/<int:pk>',views.AlbumDetail.as_view(),name='album_detail'),
    path('album_review/',views.album_review,name='album_review'),
    path('band_detail/<int:pk>',views.BandDetail.as_view(),name='band_detail'),
    path('artist_detail/<int:pk>',views.ArtistDetail.as_view(),name='artist_detail'),
    path('list_album',views.AlbumListView.as_view(),name='list_album'),
    path('list_band',views.BandListView.as_view(),name='list_band'),
    path('list_artist',views.ArtistListView.as_view(),name='list_artist'),
    path('my_view/',views.my_view,name='my_view'),
]
