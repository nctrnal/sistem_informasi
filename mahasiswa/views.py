from django.shortcuts import render, get_object_or_404, redirect
from .models import Mahasiswa
from .forms import MahasiswaForm
from django.contrib import messages
from angkatan.models import Angkatan
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication:login')

def mahasiswa(request):
    context = {
        'title': 'Mahasiswa',
        'mahasiswa_list': Mahasiswa.objects.all()
    }
    return render(request, 'mahasiswa.html', context)


def edit_mahasiswa(request, pk):
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
    mahasiswa = get_object_or_404(Mahasiswa, pk=pk)

    if request.method == 'POST':
        mahasiswa.delete()
        messages.success(
            request, f'Mahasiswa "{mahasiswa.nama}" berhasil dihapus.')
        return redirect('mahasiswa')  # Redirect to the 'mahasiswa' view

    return render(request, 'hapus_mahasiswa_confirm.html', {'mahasiswa': mahasiswa})


def tambah_mahasiswa(request):
    if request.method == 'POST':
        form = MahasiswaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Ganti 'daftar_mahasiswa' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('mahasiswa', mahasiswa.id)
    else:
        form = MahasiswaForm()


    # Konteks untuk halaman tambah_angkatan.html
    context = {
        'title': 'Mahasiswa',
        'form': form,
    }
    return render(request, 'tambah_mahasiswa.html', context)
