from django.shortcuts import render
from mahasiswa.models import Mahasiswa
from matakuliah.models import MataKuliah


def index(request):

    total_mhs = Mahasiswa.objects.count()
    prog_studi = MataKuliah.objects.values_list(
        'program_studi', flat=True).distinct().count()

    queryset1 = Mahasiswa.objects.all().count()
    queryset2 = MataKuliah.objects.all().count()

    data = {
        'data1': [queryset1],
        'data2': [queryset2],
    }

    context = {
        'title': 'Dashboard',
        'total_mhs': total_mhs,
        'prog_studi': prog_studi,
        'data': data,
    }
    return render(request, 'dashboard.html', context)
