from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('mahasiswa/', include('mahasiswa.urls')),
    path('angkatan/', include('angkatan.urls')),
    path('wisudah/', include('wisudah_yudisium.urls')),
    path('pengajar/', include('dosen_pengajar.urls')),
    path('absen/', include('absen.urls')),
    path('matakuliah/', include('matakuliah.urls')),
    path('dosenwali/', include('dosenwali.urls')),
    path('authentication/', include('authentication.urls')),
    path('user_manage/', include('user_manage.urls')),
    path('authentication/', include('authentication.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
