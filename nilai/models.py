# nilai/models.py
from django.db import models
from krs.models import KRS

class Nilai(models.Model):
    krs = models.OneToOneField(KRS, on_delete=models.CASCADE, related_name='nilai_rel')
    mata_kuliah = models.CharField(max_length=200, null=True)
    nilai = models.CharField(max_length=50)
    
    def __str__(self):
        return f"Nilai {self.krs} - {self.nilai}"
