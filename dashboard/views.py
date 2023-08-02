from django.shortcuts import render
from mahasiswa.models import Mahasiswa
from matakuliah.models import MataKuliah
from dosen_pengajar.models import DosenPengajarModel


def index(request):

    total_mhs = Mahasiswa.objects.count()
    total_dosen = DosenPengajarModel.objects.count()
    prog_studi = MataKuliah.objects.values_list(
        'program_studi', flat=True).distinct().count()
    mhs_aktif = Mahasiswa.objects.filter(status='Aktif').count()

    queryset1 = total_mhs
    queryset2 = total_dosen
    queryset3 = mhs_aktif

    data = {
        'data1': [queryset1],
        'data2': [queryset2],
        'data3': [queryset3],
    }

    context = {
        'title': 'Dashboard',
        'total_mhs': total_mhs,
        'prog_studi': prog_studi,
        'total_dosen': total_dosen,
        'mhs_aktif': mhs_aktif,
        'data': data,
    }
    return render(request, 'dashboard.html', context)
