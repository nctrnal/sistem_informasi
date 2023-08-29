from django.urls import path
from . import views

urlpatterns = [
    
    path('input_nilai/<int:krs_id>/', views.input_nilai, name='input_nilai'),
    path('', views.daftar_krs, name='daftar_krs'),
]
