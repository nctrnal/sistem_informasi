from matakuliah.models import MataKuliah
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NilaiForm
from django.contrib import messages
from dosen_pengajar.models import DosenPengajarModel
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser

@login_required(login_url='authentication:login')

def nilai(request):
    user = request.user

    try:
        dosen = DosenPengajarModel.objects.get(nrp=user.NIM)
        matkul_list = MataKuliah.objects.filter(nama_pengajar=dosen)

    except DosenPengajarModel.DoesNotExist:
        dosen = None
        matkul_list = None

    context = {
        'title': 'Data Nilai',
        'matkul_list': matkul_list,
        'dosen' : dosen,
    }
    return render(request, 'daftar.html', context)
