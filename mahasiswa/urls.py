from django.urls import path
from . import views

urlpatterns = [
    path('', views.mahasiswa, name='mahasiswa'),
    path('mahasiswa/<int:pk>/edit/', views.edit_mahasiswa, name='edit_mahasiswa'),
    path('mahasiswa/<int:pk>/hapus/',
         views.hapus_mahasiswa, name='hapus_mahasiswa'),
    path('mahasiswa/tambah/', views.tambah_mahasiswa, name='tambah_mahasiswa'),
    path('mahasiswa/<int:pk>/detail/', views.detail_mahasiswa, name='detail_mahasiswa'),
]
