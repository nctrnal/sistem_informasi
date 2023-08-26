from django.db import models

# Create your models here.


class Angkatan(models.Model):
    id = models.AutoField(primary_key=True)
    nama_angkatan = models.IntegerField()
    kurikulum = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_angkatan
