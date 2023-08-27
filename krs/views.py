from django.shortcuts import render, get_object_or_404, redirect
from authentication.models import CustomUser
from mahasiswa.models import Mahasiswa
from django.contrib import messages
from matakuliah.models import MataKuliah
from .models import KRS
from .forms import TambahKRSForm
import logging

def krs(request):

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
            krs = form.save(commit=False)
            krs.mahasiswa = user  # Set mahasiswa field sesuai user yang sedang login
            krs.save()
            form.save_m2m()
            return redirect('krs')
        else:
            logger.error('form tidak valid: %s', form.errors)
    else:
        initial_data = {'mahasiswa': request.user.NIM}  # Ganti dengan relasi yang benar
        form = TambahKRSForm(initial=initial_data)


    context = {
        'title': 'KRS',
        'mahasiswa': mahasiswa,
        'matakuliah_choices': matakuliah_choices,
        'form': form
    }
    return render(request, 'krs.html', context)

def view_krs(request):
    krs_list = KRS.objects.all()
    
    context = {
        'title': 'View All KRS',
        'krs_list': krs_list,
    }
    return render(request, 'view_krs.html', context)