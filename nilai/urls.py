from django.urls import path
from . import views

urlpatterns = [
    path('', views.nilai, name='nilai'),
]