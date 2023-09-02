from django.urls import path
from . import views

urlpatterns = [
    path('isi_krs/', views.tambah_krs, name='krs'),
    path('', views.view_krs, name='view_krs'),
    path('krs/<int:krs_id>/konfirmasi/', views.konfirmasi_krs, name='konfirmasi_krs'),
]
