from django.urls import path
from . import views

urlpatterns = [
    path('', views.matakuliah, name='matakuliah'),
    path('mata_kuliah/<int:pk>/edit/', views.edit_mata_kuliah, name='edit_mata_kuliah'),
    path('mata_kuliah/<int:pk>/hapus/', views.hapus_matkul, name='hapus_matkul'),
    path('mata_kuliah/tambah/', views.tambah_mata_kuliah, name='tambah_mata_kuliah'),
]