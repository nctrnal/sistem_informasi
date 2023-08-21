from django.db import models
from mahasiswa.models import Mahasiswa


def user_directory_path(instance, filename):
    # Untuk menyimpan foto dengan nama berdasarkan username pengguna
    return f'user_{instance}/{filename}'


class WisudahYudisiumModel(models.Model):

    nim = models.OneToOneField(
        Mahasiswa, on_delete=models.CASCADE)
    lulus_sidang = models.ImageField(upload_to='uploads/profile/',
                                     default='default.png')
    epdamo = models.ImageField(upload_to='uploads/profile/',
                               default='default.png')
    lulus_prodi = models.ImageField(upload_to='uploads/profile/',
                                    default='default.png')
    lulus_keuangan = models.ImageField(upload_to='uploads/profile/',
                                       default='default.png')
    lulus_bidkerjasama = models.ImageField(upload_to='uploads/profile/',
                                           default='default.png')
    lulus_perpus = models.ImageField(upload_to='uploads/profile/',
                                     default='default.png')
    toefl = models.ImageField(upload_to='uploads/profile/',
                              default='default.png')

    def __str__(self):
        return self.nim
