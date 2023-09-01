from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from krs.models import KRS, MataKuliah # Import model KRS
from .models import Nilai  # Import model Nilai
from .forms import NilaiForm
from .models import Nilai
from django.contrib import messages
from dosen_pengajar.models import DosenPengajarModel
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from krs.models import KRS
from mahasiswa.models import Mahasiswa
from django import forms
import logging

def daftar_krs(request):
    krs_perlu_dinilai = KRS.objects.filter(status='disetujui', nilai__isnull=True)
    
    context = {
        'title': 'Daftar KRS Perlu Dinilai',
        'krs_perlu_dinilai': krs_perlu_dinilai,
    }
    return render(request, 'daftar.html', context)

def input_nilai(request, krs_id):
    krs = get_object_or_404(KRS, id=krs_id)
    mata_kuliah_list = krs.mata_kuliah.split(',')

    if request.method == 'POST':
        nilai_list = []
        for mata_kuliah in mata_kuliah_list:
            nilai = request.POST.get(mata_kuliah)
            nilai_list.append(nilai)
        
        nilai_str = ",".join(nilai_list)
        krs.nilai = nilai_str
        krs.save()
        return redirect('daftar_krs')  # Ganti 'krs_list' dengan nama URL yang sesuai
    
<<<<<<< HEAD
    context = {
        'title': 'Input Nilai',
        'krs': krs,
    }
    return render(request, 'input_nilai.html', context)

def input_nilai(request, krs_id):
    krs = get_object_or_404(KRS, id=krs_id)
    
    if request.method == 'POST':
        for matkul in krs.mata_kuliah.all():
            nilai_input = request.POST.get(matkul.kode)
            matkul_krs = matkul  # Ganti ini dengan cara mengambil mata kuliah dari KRS yang sesuai
            nilai, created = Nilai.objects.get_or_create(krs=krs, matkul=matkul_krs)
            if nilai_input:
                nilai.nilai = nilai_input
                nilai.save()
        return redirect('daftar_krs')
    
    context = {
        'title': 'Input Nilai',
        'krs': krs,
    }
    return render(request, 'input_nilai.html', context)
=======
    nilai_formset = []
    for mata_kuliah in mata_kuliah_list:
        nilai_formset.append({'mata_kuliah': mata_kuliah})
    
    return render(request, 'input_nilai.html', {'krs': krs, 'nilai_formset': nilai_formset})






>>>>>>> c9ae4155221c72c3b96cf02bac102da11464ec45
