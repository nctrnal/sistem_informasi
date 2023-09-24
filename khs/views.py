from django.shortcuts import render
from krs.models import KRS
from mahasiswa.models import Mahasiswa
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from matakuliah.models import MataKuliah


@login_required
def khs(request):

    user = request.user

    try:
        mahasiswa_khs = Mahasiswa.objects.filter(nim=user.NIM)
    except Mahasiswa.DoesNotExist:
        mahasiswa_khs = None

    if mahasiswa_khs:
        mhs_khs = KRS.objects.filter(mahasiswa_id=user.NIM)

        nama_khs = []

        for krs in mhs_khs:
            nama_khs.extend(krs.mata_kuliah.split(', '))

        khs_unik = KRS.objects.filter(mahasiswa_id=user.NIM)

    else:
        khs_unik = []

    jurusan = request.GET.get('jurusan', None)

    if jurusan:
        if jurusan == 'semua_jurusan':
            krs_dinilai = KRS.objects.filter(nilai__isnull=False)
        else:
            krs_dinilai = KRS.objects.filter(
                mahasiswa__jurusan=jurusan, nilai__isnull=False)
    else:
        krs_dinilai = KRS.objects.filter(nilai__isnull=False)

    context = {
        'title': 'KHS',
        'krs_dinilai': krs_dinilai,
        'khs_unik': khs_unik,
    }

    return render(request, 'khs.html', context)


@login_required
def khs_detail(request, mahasiswa_id):
    # Mengambil objek KRS yang memiliki mahasiswa_id sesuai dengan parameter yang diberikan.
    krs_dinilai = get_object_or_404(
        KRS, mahasiswa_id=mahasiswa_id, nilai__isnull=False)

    # Memisahkan mata kuliah dan nilai menjadi daftar.
    matakuliah_list = krs_dinilai.mata_kuliah.split(',')
    nilai_list = krs_dinilai.nilai.split(',')
    data = zip(matakuliah_list, nilai_list)

    context = {
        'title': 'KHS',
        'mahasiswa': krs_dinilai.mahasiswa,
        'data': data,
    }

    return render(request, 'khs_detail.html', context)
