from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('add-user/', views.add_user, name='add-user'),
    path('user/<int:pk>/hapus/', views.hapus_user, name='hapus_user'),
    # ... tambahkan URL lainnya ...
]