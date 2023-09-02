from django.urls import path
from . import views

urlpatterns = [
    path('', views.pengajar, name='dosen_pengajar'),
    path('dosen_pengajar/<int:pk>/edit/',
         views.edit_pengajar, name='edit_pengajar'),
    path('dosen_pengajar/<int:pk>/hapus/',
         views.hapus_pengajar, name='hapus_pengajar'),
    path('dosen_pengajar/tambah/', views.tambah_pengajar, name='tambah_pengajar'),
    path('dosen_pengajar/<int:pk>/detail/', views.detail_dosen, name='detail_pengajar'),
]
