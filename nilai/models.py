from django.db import models

class NilaiModel(models.Model):

    pilihan_nilai = {
        ('A', 'A'),
        ('AB', 'AB'),
        ('B', 'B'),
        ('BC', 'BC'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    }

    id = models.AutoField(primary_key=True)
    nama_mahasiswa = models.CharField(max_length=100)
    nama_pengajar = models.CharField(max_length=100)
    matakuliah = models.CharField(max_length=100)
    jk = models.CharField(max_length=1)
    semester = models.CharField(max_length=100)
    angkatan = models.CharField(max_length=100)
    nilai = models.CharField(max_length=2, choices=pilihan_nilai, default='E', blank=True)


    def __str__(self):
        return self.nama_mahasiswa

