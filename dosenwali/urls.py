from django.urls import path
from . import views

urlpatterns = [
    path('', views.dosenwali, name='dosenwali'),
    #     path('dosenwali/<int:pk>/edit/',
    #          views.edit_doswal, name='edit_doswal'),
    path('dosenwali/<int:pk>/hapus/',
         views.hapus_doswal, name='hapus_doswal'),
    path('dosenwali/tambah/', views.tambah_doswal, name='tambah_doswal'),
]
