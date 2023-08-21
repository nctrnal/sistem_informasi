from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user-list'),
    path('add-user/', views.add_user, name='add-user'),
    # ... tambahkan URL lainnya ...
]