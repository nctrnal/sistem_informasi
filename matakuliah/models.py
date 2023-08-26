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

<<<<<<< HEAD
<<<<<<< HEAD
    pilihan_tipe = {
        ("Teori", "Teori"),
        ("Praktikum", "Praktikum")
    }

=======
>>>>>>> e44767ec837788c4ef383bfceb6177d8c04b4d7c
=======
>>>>>>> e44767ec837788c4ef383bfceb6177d8c04b4d7c
    kode_mata_kuliah = models.CharField(max_length=10)
    nama_mata_kuliah = models.CharField(max_length=100, choices=pilihan_matkul)
    jumlah_sks = models.IntegerField()
    program_studi = models.CharField(max_length=50)
<<<<<<< HEAD
<<<<<<< HEAD
    tipe = models.CharField(max_length=100, blank=True)
    kuota = models.IntegerField(blank=True, default=30)
    kelas = models.CharField(max_length=100, default="A")
=======
    kelas = models.CharField(max_length=10)
>>>>>>> e44767ec837788c4ef383bfceb6177d8c04b4d7c
=======
    kelas = models.CharField(max_length=10)
>>>>>>> e44767ec837788c4ef383bfceb6177d8c04b4d7c
    nama_pengajar = models.ForeignKey(
        DosenPengajarModel, on_delete=models.CASCADE, related_name='mata_kuliah_list')

    def __str__(self):
        return self.nama_mata_kuliah
