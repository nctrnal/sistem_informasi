from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

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
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
