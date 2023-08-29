from django.db import models

class AbsenModel(models.Model):
    id = models.AutoField(primary_key=True)
    nama_matkul = models.CharField()
    nama_dosen = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_matkul
