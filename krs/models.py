from django.db import models

class KRS(models.Model):
    mahasiswa = models.CharField(max_length=100)
    mata_kuliah = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='belum di acc')

    def __str__(self):
        return f"{self.mahasiswa} - {self.mata_kuliah}"