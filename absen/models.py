from django.db import models
from mahasiswa.models import Mahasiswa
from dosen_pengajar.models import DosenPengajarModel
from django.utils import timezone


class Absen(models.Model):

    dosen = models.ForeignKey(DosenPengajarModel, on_delete=models.CASCADE)
    # mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mahasiswa = models.CharField(max_length=100, blank=True)
    mata_kuliah = models.CharField(max_length=100, blank=True)
    kehadiran = models.CharField(max_length=20, default='Tidak Hadir')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.mahasiswa} - {self.kehadiran}"
