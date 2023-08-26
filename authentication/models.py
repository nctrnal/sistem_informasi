from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from functools import wraps
from django.http import HttpResponseForbidden

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'NIM'
    
    role = models.CharField(max_length=50)
    NIM = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=50)
    
    custom_groups = models.ManyToManyField(Group, related_name='custom_users')
    custom_user_permissions = models.ManyToManyField(
        Permission, related_name='custom_users_permissions'
    )
    
    def __str__(self):
        return self.username

    def role_required(self, role_name):
        def decorator(view_func):
            @wraps(view_func)
            def _wrapped_view(request, *args, **kwargs):
                if self.is_authenticated and self.role == role_name:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini.")
            return _wrapped_view
        return decorator