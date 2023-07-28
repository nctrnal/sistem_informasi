from django.db import models


def user_directory_path(instance, filename):
    # Untuk menyimpan foto dengan nama berdasarkan username pengguna
    return f'user_{instance.nama}/{filename}'


class DosenWaliModel(models.Model):

    jenis_kelamin = [
        ('Laki-Laki', 'L'),
        ('Perempuan', 'P'),
    ]

    nrp = models.IntegerField(primary_key=True)
    nama_doswal = models.CharField(max_length=100)
    jk = models.CharField(max_length=20, choices=jenis_kelamin, default='L')
    prodi = models.CharField(max_length=100)
    kelas = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_doswal
