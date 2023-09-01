from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Absen
from mahasiswa.models import Mahasiswa
from krs.models import KRS
from dosen_pengajar.models import DosenPengajarModel
from matakuliah.models import MataKuliah
from .forms import AbsenForm
from django import forms
from django.forms import formset_factory
from django.forms.models import inlineformset_factory, modelformset_factory
import logging


@login_required(login_url='authentication:login')
def absen(request):
    user = request.user

    # Cari dosen berdasarkan NIM dari user yang sedang login
    try:
        dosen = DosenPengajarModel.objects.get(nrp=user.NIM)

    except DosenPengajarModel.DoesNotExist:
        dosen = None

    # Jika ditemukan dosen, ambil daftar mata kuliah yang diajar oleh dosen tersebut
    if dosen:
        krs_disetujui = KRS.objects.filter(status='disetujui')

        nama_mk_disetujui = []

        for krs in krs_disetujui:
            nama_mk_disetujui.extend(krs.mata_kuliah.split(', '))

        # hapus duplikat mk
        nama_mk_disetujui_unik = list(set(nama_mk_disetujui))

        mk_diajar = MataKuliah.objects.filter(
            nama_mata_kuliah__in=nama_mk_disetujui_unik, nama_pengajar=dosen)

    else:
        mk_diajar = []

    context = {
        'title': 'Absen Dosen Mahasiswa',
        'mk_diajar': mk_diajar,
        'dosen': dosen
    }

    return render(request, 'view_absen.html', context)


def input_absen(request, id):
    logger = logging.getLogger(__name__)
    user = request.user

    try:
        dosen = DosenPengajarModel.objects.get(nrp=user.NIM)
        mata_kuliah_diajar = MataKuliah.objects.filter(nama_pengajar_id=dosen)
    except DosenPengajarModel.DoesNotExist:
        dosen = None
        mata_kuliah_diajar = []

    #ambil id mata kuliah yang dipilih
    if id:
        mata_kuliah_terpilih = MataKuliah.objects.get(id=id)
    else:
        mata_kuliah_terpilih = None

    #Modifikasi ini untuk mendapatkan data mahasiswa yang mengambil mata kuliah tertentu
    if id:
        mata_kuliah_terpilih = MataKuliah.objects.get(id=id)
        mahasiswa_mengambil = KRS.objects.filter(mata_kuliah=mata_kuliah_terpilih, status='disetujui')
    else:
        mahasiswa_mengambil = []

    if request.method == 'GET':
        mahasiswa_awal = list(set([krs.mahasiswa.nama for krs in mahasiswa_mengambil]))
        form = AbsenForm(initial={
            'dosen': dosen.nrp,
            'mahasiswa': mahasiswa_awal,  # Atau isi dengan data mahasiswa default jika ada
            'mata_kuliah': mata_kuliah_terpilih,  # Isi dengan ID mata kuliah terpilih jika ada
        })

    elif request.method == 'POST':
        form = AbsenForm(request.POST)
        if form.is_valid():
            selected_mata_kuliah = form.cleaned_data['mata_kuliah']


            # Loop melalui semua mata kuliah yang dipilih
            for mata_kuliah in selected_mata_kuliah:
                # Dapatkan semua mahasiswa yang mengambil mata kuliah ini
                mahasiswa_mengambil = KRS.objects.filter(
                    mata_kuliah=mata_kuliah, status='disetujui')

                # Loop melalui semua mahasiswa dan simpan kehadiran mereka
                for mahasiswa in mahasiswa_mengambil:
                    kehadiran = form.cleaned_data['kehadiran']
                    Absen.objects.create(dosen=dosen.nrp, mahasiswa=mahasiswa,
                                         mata_kuliah=mata_kuliah_terpilih, kehadiran=kehadiran)
            form.save()

            return redirect('absen')
        else:
            logger.error('Form tidak valid: %s', form.errors)
    else:
        form = AbsenForm()

    context = {
        'title': 'Absen',
        'dosen': dosen,
        'mata_kuliah_diajar': mata_kuliah_diajar,
        'form': form,
        'mahasiswa_mengambil': mahasiswa_mengambil,
        'mata_kuliah': mata_kuliah_terpilih,

    }
    return render(request, 'absen.html', context)