from django.urls import path
from . import views

urlpatterns = [
    path('', views.dosenwali, name='dosenwali'),
]