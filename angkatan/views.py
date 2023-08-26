from django.shortcuts import render
from .models import Angkatan
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AngkatanForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication:login')

def angkatan(request):
    context = {
        'title': 'Angkatan',
        'angkatan_list': Angkatan.objects.all()
    }
    return render(request, 'angkatan.html', context)


def edit_angkatan(request, pk):
    angkatan = get_object_or_404(Angkatan, pk=pk)

    if request.method == 'POST':
        form = AngkatanForm(request.POST, instance=angkatan)
        if form.is_valid():
            form.save()
            return redirect('angkatan')
    else:
        form = AngkatanForm(instance=angkatan)

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Angkatan',
        'form': form,
    }

    return render(request, 'edit_angkatan.html', context)


def hapus_angkatan(request, pk):
    angkatan = get_object_or_404(Angkatan, pk=pk)

    if request.method == 'POST':
        angkatan.delete()
        messages.success(
            request, f'angkatan "{angkatan.nama_angkatan}" berhasil dihapus.')
        return redirect('angkatan')  # Redirect to the 'daftar_matkul' view

    return render(request, 'hapus_angkatan_confirm.html', {'angkatan': angkatan})


def tambah_angkatan(request):
    if request.method == 'POST':
        form = AngkatanForm(request.POST)
        if form.is_valid():
            form.save()
            # Ganti 'daftar_matkul' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('angkatan')
    else:
        form = AngkatanForm()

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Angkatan',
        'form': form,
    }
    return render(request, 'tambah_angkatan.html', context)
