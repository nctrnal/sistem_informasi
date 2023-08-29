from matakuliah.models import MataKuliah
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NilaiForm
from .models import NilaiModel
from django.contrib import messages
from dosen_pengajar.models import DosenPengajarModel
from django.contrib.auth.decorators import login_required
from authentication.models import CustomUser
from krs.models import KRS
from mahasiswa.models import Mahasiswa
from django import forms
import logging

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

def input_nilai(request, id):
    logger = logging.getLogger(__name__)
    mata_kuliah = get_object_or_404(MataKuliah, id=id)
    mahasiswas = Mahasiswa.objects.all()
    user = request.user  # Anda perlu mengganti ini dengan cara yang sesuai untuk mendapatkan Dosen saat ini
    
    try:
        dosen = DosenPengajarModel.objects.get(nrp=user.NIM)
        matkul_list = MataKuliah.objects.filter(nama_pengajar=dosen)
        NilaiFormSet = forms.formset_factory(NilaiForm, extra=len(mahasiswas))

        if request.method =='POST':
            formset = NilaiFormSet(request.POST)
            if formset.is_valid():
                # nilai = form.save(commit=False)
                # nilai.mata_kuliah = mata_kuliah
                # nilai.save()
                nilai = form.cleaned_data['nama_mata_kuliah']
                mahasiswa = form.cleaned_data['nama_mahasiswa']
                # Simpan nilai ke dalam database
                NilaiModel.objects.create(mahasiswa=mahasiswa, dosen=dosen, nilai=nilai)
                return redirect('nilai')
            else:
                logger.error('form tidak valid: %s', form.errors)

        else:
            formset = NilaiForm(instance=mata_kuliah)

    except DosenPengajarModel.DoesNotExist:
        dosen = None
        matkul_list = None

    context ={
        'title': 'Data Nilai',
        'matkul_list':matkul_list,
        'formset' : formset

    }

    return render(request, 'nilaimatkul.html', context)