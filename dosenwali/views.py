from django.shortcuts import render, redirect, get_object_or_404
from .forms import DosenWaliForm
from .models import DosenWaliModel
from django.contrib import messages


def dosenwali(request):
    context = {
        'title': 'Dosen Wali',
        'doswal_list': DosenWaliModel.objects.all(),
    }
    return render(request, 'dosenwali.html', context)


def edit_doswal(request, pk):
    doswal = get_object_or_404(DosenWaliModel, pk=pk)

    if request.method == 'POST':
        form = DosenWaliForm(
            request.POST, instance=doswal)
        if form.is_valid():
            form.save()
            return redirect('dosenwali')
    else:
        form = DosenWaliForm(instance=dosenwali)

    # Konteks untuk halaman edit_mahasiswa.html
    context = {
        'title': 'Dosen Wali',
        'form': form,
    }

    return render(request, 'edit_doswal.html', context)


def hapus_doswal(request, pk):
    doswal = get_object_or_404(DosenWaliModel, pk=pk)

    if request.method == 'POST':
        doswal.delete()
        messages.success(
            request, f'Dosen wali "{doswal.nama_doswal}" berhasil dihapus.')
        return redirect('dosenwali')  # Redirect to the 'mahasiswa' view

    return render(request, 'hapus_doswal.html', {'doswal': doswal})


def tambah_doswal(request):
    if request.method == 'POST':
        form = DosenWaliForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Ganti 'daftar_mahasiswa' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('dosenwali')
    else:
        form = DosenWaliForm()

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Dosen Wali',
        'form': form,
    }
    return render(request, 'tambah_doswal.html', context)
