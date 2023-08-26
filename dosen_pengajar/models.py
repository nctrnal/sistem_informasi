from django.db import models


def user_directory_path(instance, filename):
    # Untuk menyimpan foto dengan nama berdasarkan username pengguna
    return f'user_{instance.nama}/{filename}'


class DosenPengajarModel(models.Model):

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

    nrp = models.CharField(primary_key=True)
    foto = models.ImageField(upload_to='uploads/profile/',
                             default='default.png')
    nama = models.CharField(max_length=100)
    jk = models.CharField(
        max_length=20, choices=jenis_kelamin, default='Laki-Laki')
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    alamat = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    kelas = models.CharField(max_length=100, default='3TI A')
    status = models.CharField(
        max_length=100, choices=pilihan_status, default='A')
    prodi = models.CharField(max_length=100)
    agama = models.CharField(
        max_length=50, choices=pilihan_agama, default='Islam')

    def __str__(self):
        return self.nama
