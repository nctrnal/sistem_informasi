from django.shortcuts import render, redirect, get_object_or_404
from .models import CutiModel
from .forms import CutiForm
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import logging


@login_required(login_url='authentication:login')

def cuti(request):
    context = {
        'title': 'Pengajuan Cuti',
        'cuti_list': CutiModel.objects.all()
    }

    return render(request, 'cuti.html', context)

def ajukan_cuti(request):

    logger = logging.getLogger(__name__)
    nama = request.user.username

    if request.method == 'POST':
        form = CutiForm(request.POST, request.FILES)
        if form.is_valid():
            cuti = form.save(commit=False)
            cuti.nama = nama
            cuti.save()
            messages.success(request, f'Cuti berhasil diajukan, silahkan tunggu respon pihak prodi')
            # messages.error(request, f'Mahasiswa gagal ditambahkan')
            # Ganti 'daftar_mahasiswa' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('cuti')
        else:
            logger.error('Form tidak valid: %s', form.errors)
    else:
        initial_data = {'nama': nama}
        form = CutiForm(initial=initial_data)
        print(initial_data)


    # Konteks untuk halaman tambah_angkatan.html
    context = {
        'title': 'Ajukan Cuti',
        'form': form,
    }
    return render(request, 'ajukan_cuti.html', context)

def proses_cuti(request, pk):
    cuti = get_object_or_404(CutiModel, pk=pk)
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        form = CutiForm(request.POST,request.FILES, instance=cuti)

        form.fields['nama'].widget = forms.HiddenInput()
        form.fields['nama'].initial = cuti.nama

        if form.is_valid():
            form.save()
            return redirect('cuti')
        else:
            logger.error('Form tidak valid: %s', form.errors)
    else:
        form = CutiForm(instance=cuti)
    
    form.fields['nama'].widget.attrs['readonly'] = True
    form.fields['tanggal_mulai'].widget.attrs['readonly'] = True
    form.fields['lama_cuti'].widget.attrs['readonly'] = True
    form.fields['keterangan'].widget.attrs['readonly'] = True
    form.fields['syarat_cuti'].widget.attrs['readonly'] = True

    # Konteks
    context = {
        'title': 'Pengajuan Cuti',
        'form': form,
    }

    return render(request, 'proses_cuti.html', context)