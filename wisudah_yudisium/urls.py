from django.urls import path
from . import views

urlpatterns = [
    path('', views.wisudah, name='wisudah'),
]