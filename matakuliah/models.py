# models.py
from django.db import models
from dosen_pengajar.models import DosenPengajarModel


class MataKuliah(models.Model):

    pilihan_matkul= {
        ('Sistem Informasi', 'Sistem Informasi'),
        ('Desain Web', 'Desain Web'),
        ('Struktur Data', 'Struktur Data'),
        ('Algoritma Pemrograman', 'Algoritma Pemrograman'),
        ('Organisasi Arsitektur Komputer', 'Organisasi Arsitektur Komputer'),
        ('Struktur Data', 'Struktur Data'),
        ('Matematika Teknik', 'Matematika Teknik'),
    }

    kode_mata_kuliah = models.CharField(max_length=10)
    nama_mata_kuliah = models.CharField(max_length=100, choices=pilihan_matkul)
    jumlah_sks = models.IntegerField()
    program_studi = models.CharField(max_length=50)
    kelas = models.CharField(max_length=10)
    nama_pengajar = models.ForeignKey(
        DosenPengajarModel, on_delete=models.CASCADE, related_name='mata_kuliah_list')

    def __str__(self):
        return self.nama_mata_kuliah
