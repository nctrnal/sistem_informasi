from django.urls import path
from . import views

urlpatterns = [
    path('', views.khs, name='khs'),
    path('<int:mahasiswa_id>/', views.khs_detail, name='khs_detail'),
]