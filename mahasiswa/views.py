from django.shortcuts import render, get_object_or_404, redirect
from .models import Mahasiswa
from .forms import MahasiswaForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import logging
import string
import random
from authentication.models import CustomUser
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

CustomUser = get_user_model()


@login_required(login_url='authentication:login')

def mahasiswa(request):
    jurusan = request.GET.get('jurusan', None)

    if jurusan:
        if jurusan == 'semua_jurusan':
            mahasiswa_list = Mahasiswa.objects.all()
        else:
            mahasiswa_list = Mahasiswa.objects.filter(jurusan=jurusan)
    else:
        mahasiswa_list = Mahasiswa.objects.all()

    context = {
        'title': 'Mahasiswa',
        'mahasiswa_list': mahasiswa_list
    }
    return render(request, 'mahasiswa.html', context)


def edit_mahasiswa(request, pk):
    custom_user = CustomUser.objects.get(username=request.user.username)  # Ganti dengan field yang sesuai
    if custom_user.role != 'akademik':
        return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini")
    
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)

    if request.method == 'POST':
        form = MahasiswaForm(request.POST, request.FILES, instance=mahasiswa)
        if form.is_valid():
            form.save()
            return redirect('mahasiswa')
    else:
        form = MahasiswaForm(instance=mahasiswa)

    # Konteks untuk halaman edit_mahasiswa.html
    context = {
        'title': 'Mahasiswa',
        'form': form,
    }

    return render(request, 'edit_mahasiswa.html', context)


def hapus_mahasiswa(request, pk):
    custom_user = CustomUser.objects.get(username=request.user.username)  # Ganti dengan field yang sesuai
    if custom_user.role != 'akademik':
        return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini")
    
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)

    if request.method == 'POST':
        mahasiswa.delete()
        messages.success(
            request, f'Mahasiswa "{mahasiswa.nama}" berhasil dihapus.')
        return redirect('mahasiswa')  # Redirect to the 'mahasiswa' view

    return render(request, 'hapus_mahasiswa_confirm.html', {'mahasiswa': mahasiswa})

def tambah_mahasiswa(request):
    # custom_user = CustomUser.objects.get(username=request.user.username)  # Ganti dengan field yang sesuai
    # if custom_user.role != 'akademik':
    #     return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini")

    logger = logging.getLogger(__name__)
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, request.FILES)
        if form.is_valid():
            mahasiswa = form.save()

            #ambil NIM dari objek mahasiswa
            username = mahasiswa.nim

            try:
                CustomUser = get_user_model()
                existing_user = CustomUser.objects.get(NIM=username)
                
                # Perbarui atribut-atribut objek existing_user dengan data yang baru.
                existing_user.email = mahasiswa.email
                existing_user.role = 'mahasiswa'  # Gantilah dengan role yang sesuai
                existing_user.status = 'aktif'  # Gantilah dengan status yang sesuai
                existing_user.save()

                messages.success(request, f'Mahasiswa berhasil diperbarui')
            except CustomUser.DoesNotExist:
                # Buat objek CustomUser baru karena NIM belum ada.
                password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                custom_user = CustomUser.objects.create_user(username=username, password=password)
                custom_user.email = mahasiswa.email
                custom_user.role = 'mahasiswa'  # Gantilah dengan role yang sesuai
                custom_user.status = 'aktif'  # Gantilah dengan status yang sesuai
                custom_user.save()
                messages.success(request, f'Mahasiswa berhasil ditambahkan')
                # messages.error(request, f'Mahasiswa gagal ditambahkan')
                # Ganti 'daftar_mahasiswa' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('mahasiswa')
        else:
            logger.error('Form tidak valid: %s', form.errors)
    else:
        form = MahasiswaForm()


    # Konteks untuk halaman tambah_angkatan.html
    context = {
        'title': 'Mahasiswa',
        'form': form,
    }
    return render(request, 'tambah_mahasiswa.html', context)

def detail_mahasiswa(request, pk):
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)
    context = {'title': 'Mahasiswa',
        'mahasiswa': mahasiswa}
    return render(request, 'detail_mahasiswa.html', context)
