from django.urls import path
from . import views

urlpatterns = [
    path('', views.krs, name='krs'),
]