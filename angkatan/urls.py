from django.urls import path
from . import views

urlpatterns = [
    path('', views.angkatan, name='angkatan'),
    path('angkatan/<int:pk>/edit/', views.edit_angkatan, name='edit_angkatan'),
    path('angkatan/<int:pk>/hapus/', views.hapus_angkatan, name='hapus_angkatan'),
    path('angkatan/tambah/', views.tambah_angkatan, name='tambah_angkatan'),
]