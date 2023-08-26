from matakuliah.models import MataKuliah
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NilaiForm
from django.contrib import messages
from dosen_pengajar.models import DosenPengajarModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='authentication:login')

def nilai(request):
    matkul_list = MataKuliah.objects.all()
    context = {
        'title': 'Data Nilai',
        'matkul_list': matkul_list
    }
    return render(request, 'daftar.html', context)
