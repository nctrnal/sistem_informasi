from django.db import models
from mahasiswa.models import Mahasiswa


class KRS(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    mata_kuliah = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='belum disetujui')
    nilai = models.CharField(max_length=20, null=True, blank=True)  # Contoh DecimalField untuk nilai

    def __str__(self):
        return f"{self.mahasiswa} - {self.mata_kuliah}"

class MataKuliah(models.Model):
    kode = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    jumlah_sks = models.IntegerField(default=0)

    def __str__(self):
        return self.nama
    