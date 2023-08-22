from django.db import models

def user_directory_path(instance, filename):
    # Untuk menyimpan foto dengan nama berdasarkan username pengguna
    return f'user_{instance.nama}/{filename}'


class CutiModel(models.Model):
    pilihan_status = [
        ('Status', 'Status'),
        ('Disetujui', 'Disetujui'),
        ('Ditolak', 'Ditolak')
    ]

    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100, blank=True)
    tanggal_mulai = models.DateField()
    lama_cuti = models.CharField(max_length=100)
    syarat_cuti = models.FileField(upload_to='uploads/cuti/')
    keterangan = models.CharField(max_length=100)
    status_cuti = models.CharField(
        max_length=100, choices=pilihan_status, default='Status', blank=True)

    def __str__(self):
        return self.nama