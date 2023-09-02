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

    # Inisialisasi mata_kuliah_terpilih dan mahasiswa_mengambil
    mata_kuliah_terpilih = None
    mahasiswa_mengambil = []

    if id:
        try:
            mata_kuliah_terpilih = MataKuliah.objects.get(id=id)
            # Dapatkan semua mahasiswa yang mengambil mata kuliah ini dan sudah disetujui
            mahasiswa_mengambil = KRS.objects.filter(mata_kuliah=mata_kuliah_terpilih, status='disetujui')
        except MataKuliah.DoesNotExist:
            pass

    AbsenFormSet = formset_factory(AbsenForm, extra=0)

    if request.method == 'POST':
        formset = AbsenFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                kehadiran = form.cleaned_data['kehadiran']
                mahasiswa = form.cleaned_data['mahasiswa']

                dosen_instance = DosenPengajarModel.objects.get(nrp=dosen.nrp)

                Absen.objects.create(dosen=dosen_instance , mahasiswa=mahasiswa,
                                     mata_kuliah=mata_kuliah_terpilih, kehadiran=kehadiran)

            return redirect('absen')
        else:
            logger.error('Salah satu atau lebih formulir tidak valid.')
    else:
        initial_data = [{'dosen': dosen, 'mahasiswa': mahasiswa.mahasiswa.nama, 'mata_kuliah': mata_kuliah_terpilih,
                         'nim_mhs':mahasiswa.mahasiswa.nim, 'angkatan':mahasiswa.mahasiswa.angkatan}
                        for mahasiswa in mahasiswa_mengambil]
        formset = AbsenFormSet(initial=initial_data)

    context = {
        'title': 'Absen',
        'dosen': dosen,
        'mata_kuliah_diajar': mata_kuliah_diajar,
        'formset': formset,
        'mata_kuliah': mata_kuliah_terpilih,
    }
    return render(request, 'absen.html', context)
