from django.urls import path
from . import views

urlpatterns = [
    path('', views.pengajar, name='pengajar'),
]