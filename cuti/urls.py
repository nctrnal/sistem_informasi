from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuti, name='cuti'),
    path('cuti/tambah/', views.ajukan_cuti, name='ajukan_cuti'),
    path('cuti/<int:pk>/edit/', views.proses_cuti, name='proses_cuti'),
]