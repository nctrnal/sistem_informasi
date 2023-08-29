from django.db import models
from krs.models import KRS, MataKuliah

class Nilai(models.Model):
    krs = models.ForeignKey(KRS, on_delete=models.CASCADE, related_name='nilais')  # Menggunakan related_name 'nilais'
    matkul = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    nilai = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.krs.mahasiswa} - {self.matkul.nama} - Nilai: {self.nilai}"
