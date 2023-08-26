from django.db import models

# Create your models here.


class TahunAjaranModel(models.Model):
    pilihan_semester = [
        ('Genap', 'Genap'),
        ('Ganjil', 'Ganjil')
    ]

    id = models.AutoField(primary_key=True)
    tahun_ajaran = models.CharField(max_length=100)
    ajaran_semester = models.CharField(max_length=100, choices=pilihan_semester)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tahun_ajaran