from django.urls import path
from . import views

urlpatterns = [
    path('', views.absen, name='absen'),
    # path('', views.detail_mk, name='detail_mk'),
    path('input_absen/<int:id>/', views.input_absen, name='input_absen'),
]