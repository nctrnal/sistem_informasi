from .models import MataKuliah
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MataKuliahForm
from django.contrib import messages


def matakuliah(request):
    context = {
        'title': 'Mata kuliah',
        'mata_kuliah_list': MataKuliah.objects.all()
    }
    return render(request, 'matakuliah.html', context)


def edit_mata_kuliah(request, pk):
    mata_kuliah = get_object_or_404(MataKuliah, pk=pk)

    if request.method == 'POST':
        form = MataKuliahForm(request.POST, instance=mata_kuliah)
        if form.is_valid():
            form.save()
            return redirect('matakuliah')
    else:
        form = MataKuliahForm(instance=mata_kuliah)

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Mata kuliah',
        'form': form,
    }

    return render(request, 'edit_matkul.html', context)


def hapus_matkul(request, pk):
    mata_kuliah = get_object_or_404(MataKuliah, pk=pk)

    if request.method == 'POST':
        mata_kuliah.delete()
        messages.success(
            request, f'Mata kuliah "{mata_kuliah.nama_mata_kuliah}" berhasil dihapus.')
        return redirect('matakuliah')  # Redirect to the 'daftar_matkul' view

    return render(request, 'hapus_matkul_confirm.html', {'mata_kuliah': mata_kuliah})


def tambah_mata_kuliah(request):
    if request.method == 'POST':
        form = MataKuliahForm(request.POST)
        if form.is_valid():
            form.save()
            # Ganti 'daftar_matkul' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('matakuliah')
    else:
        form = MataKuliahForm()

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Mata kuliah',
        'form': form,
    }
    return render(request, 'tambah_mata_kuliah.html', context)
