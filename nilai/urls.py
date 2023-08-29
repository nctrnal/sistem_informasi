from django.urls import path
from . import views

urlpatterns = [
    path('', views.nilai, name='nilai'),
    path('input_nilai/<int:id>/edit/', views.input_nilai, name='input_nilai')
]