from django.db import models


def user_directory_path(instance, filename):
    # Untuk menyimpan foto dengan nama berdasarkan username pengguna
    return f'user_{instance.nama}/{filename}'


class Mahasiswa(models.Model):
    nim = models.IntegerField(primary_key=True)
    foto = models.ImageField(upload_to='uploads/profile/',
                             default='default.png')
    nama = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    angkatan = models.IntegerField()
    semester = models.IntegerField()
    jk = models.CharField(max_length=1)
    agama = models.CharField(max_length=20)
    beasiswa = models.CharField(max_length=20)

    def __str__(self):
        return self.mahasiswa
