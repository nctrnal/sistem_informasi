from django.db import models
from angkatan.models import Angkatan
from authentication.models import CustomUser

def user_directory_path(instance, filename):
    # Untuk menyimpan foto dengan nama berdasarkan username pengguna
    return f'user_{instance.nama}/{filename}'


class Mahasiswa(models.Model):

    pilihan_status = [
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif')
    ]

    jenis_kelamin = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
    ]
    pilihan_agama = [
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katolik', 'Katolik'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
        ('Konghucu', 'Konghucu'),
    ]
    pilihan_jurusan = [
        ('Teknologi Informasi', 'Teknologi Informasi'),
        ('Akuntansi', 'Akuntansi'),
        ('Teknik Elektro', 'Teknik Elektro'),
        ('Mekatronika', 'Mekatronika'),
    ]

    nim = models.IntegerField(primary_key=True) 
    foto = models.ImageField(upload_to='uploads/profile/',
                             default='default.png')
    nama = models.CharField(max_length=100)
    jk = models.CharField(max_length=20, choices=jenis_kelamin, default='L')
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.CharField(max_length=1000, null=True)
    email = models.CharField(max_length=1000, null=True)
    doswal = models.CharField(max_length=1000, null=True)
    status = models.CharField(
        max_length=100, choices=pilihan_status, default='Aktif')
    angkatan = models.CharField()
    semester = models.IntegerField()
    agama = models.CharField(
        max_length=50, choices=pilihan_agama, default='Islam')
    beasiswa = models.CharField(max_length=20)
    jurusan = models.CharField(
        max_length=50, choices=pilihan_jurusan, default='Teknologi Informasi')

    def __str__(self):
        return self.nama
