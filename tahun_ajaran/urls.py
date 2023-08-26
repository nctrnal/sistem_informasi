from django.urls import path
from . import views

urlpatterns = [
    path('', views.tahunajaran, name='tahun_ajaran'),
    path('tahun_ajaran/<int:pk>/edit/', views.edit_tahunajaran, name='edit_tahunajaran'),
    path('tahun_ajaran/<int:pk>/hapus/', views.hapus_tahunajaran, name='hapus_tahunajaran'),
    path('tahun_ajaran/tambah/', views.tambah_tahunajaran, name='tambah_tahunajaran'),
]