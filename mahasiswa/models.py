from django.db import models


class Mahasiswa(models.Model):
    nim = models.IntegerField(primary_key=True)
    foto = models.CharField(blank=True, null=True, max_length=1000)
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
