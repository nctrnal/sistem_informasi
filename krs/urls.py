from django.urls import path
from . import views

urlpatterns = [
    path('', views.krs, name='krs'),
    path('view_krs/', views.view_krs, name='view_krs'),
]