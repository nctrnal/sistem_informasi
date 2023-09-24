from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from mahasiswa.models import Mahasiswa
from django.contrib import messages
from matakuliah.models import MataKuliah
from .models import KRS, MataKuliah
from .forms import TambahKRSForm
import logging

def tambah_krs(request):
    
    logger = logging.getLogger(__name__)
    user = request.user

    try:
        mahasiswa = Mahasiswa.objects.get(nim=user.NIM)
    except Mahasiswa.DoesNotExist:
        mahasiswa = None

    matakuliah_choices = MataKuliah.objects.all()
    

    if request.method == 'POST':
        form = TambahKRSForm(request.POST)
        if form.is_valid():
            selected_mata_kuliah = form.cleaned_data['mata_kuliah']
            nama_mata_kuliah = [mata_kuliah.nama_mata_kuliah for mata_kuliah in selected_mata_kuliah]
            nama_mata_kuliah_str = ", ".join(nama_mata_kuliah)
            
            krs = KRS(mahasiswa=mahasiswa, mata_kuliah=nama_mata_kuliah_str, status='belum disetujui')
            krs.save()
            return redirect('view_krs')
        else:
            logger.error('form tidak valid: %s', form.errors)
    else:
        initial_data = {'mahasiswa': mahasiswa}  # Set mahasiswa field sesuai user yang sedang login
        form = TambahKRSForm(initial=initial_data)

    context = {
        'title': 'KRS',
        'mahasiswa': mahasiswa,
        'matakuliah_choices': matakuliah_choices,
        'form': form
    }
    return render(request, 'krs.html', context)

def view_krs(request):
    user = request.user

    #cari mahasiswa
    try:
        mahasiswa_krs = Mahasiswa.objects.get(nim=user.NIM)

    except Mahasiswa.DoesNotExist:
        mahasiswa_krs = None
    
    if mahasiswa_krs:
        krs_diambil = KRS.objects.filter(mahasiswa_id=user.NIM)

        nama_krs = []

        for krs in krs_diambil:
            nama_krs.extend(krs.mata_kuliah.split(', '))

        krs_unik = KRS.objects.filter(mahasiswa_id=user.NIM)

    else:
        krs_unik = []

    jurusan = request.GET.get('jurusan', None)

    if jurusan:
        if jurusan == 'semua_jurusan':
            krs_list = KRS.objects.all()
        else:
            krs_list = KRS.objects.filter(mahasiswa__jurusan=jurusan)
    else:
        krs_list = KRS.objects.all()

    context = {
        'title': 'View KRS',
        'krs_list': krs_list,
        'krs_unik': krs_unik,
    }
    return render(request, 'view_krs.html', context)



def konfirmasi_krs(request, krs_id):
    krs = get_object_or_404(KRS, id=krs_id)
    mata_kuliah_list = krs.mata_kuliah.split(', ')
    total_mata_kuliah = len(mata_kuliah_list)

    if request.method == 'POST':
        total_konfirmasi = 0
        for mata_kuliah in mata_kuliah_list:
            if request.POST.get(mata_kuliah) == 'on':
                total_konfirmasi += 1
        
        if total_konfirmasi == total_mata_kuliah:
            krs.status = 'disetujui'
            krs.save()
            return redirect('view_krs')  # Ganti dengan URL yang sesuai

    context = {
        'title': 'Konfirmasi KRS',
        'krs': krs,
        'mata_kuliah_list': mata_kuliah_list,
        'total_mata_kuliah': total_mata_kuliah,
    }
    return render(request, 'konfirmasi_krs.html', context)
