from django.urls import path
from . import views

urlpatterns = [
    path('', views.tambah_krs, name='krs'),
    path('view_krs/', views.view_krs, name='view_krs'),
    path('krs/<int:krs_id>/konfirmasi/', views.konfirmasi_krs, name='konfirmasi_krs'),
]