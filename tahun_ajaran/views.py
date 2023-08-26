from django.shortcuts import render
from .models import TahunAjaranModel
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TahunAjaranForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication:login')

def tahunajaran(request):
    context = {
        'title': 'Tahun Ajaran',
        'tahunajaran_list': TahunAjaranModel.objects.all()
    }
    return render(request, 'tahunajaran.html', context)


def edit_tahunajaran(request, pk):
    tahunajaran = get_object_or_404(TahunAjaranModel, pk=pk)

    if request.method == 'POST':
        form = TahunAjaranForm(request.POST, instance=tahunajaran)
        if form.is_valid():
            form.save()
            return redirect('tahun_ajaran')
    else:
        form = TahunAjaranForm(instance=tahunajaran)

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Tahun Ajaran',
        'form': form,
    }

    return render(request, 'edit_tahunajaran.html', context)


def hapus_tahunajaran(request, pk):
    tahunajaran = get_object_or_404(TahunAjaranModel, pk=pk)

    if request.method == 'POST':
        tahunajaran.delete()
        messages.success(
            request, f'Tahun Ajaran "{tahunajaran.tahun_ajaran}" berhasil dihapus.')
        return redirect('tahunajaran')  # Redirect to the 'daftar_matkul' view

    return render(request, 'hapus_tahunajaran.html', {'tahunajaran': tahunajaran})


def tambah_tahunajaran(request):
    if request.method == 'POST':
        form = TahunAjaranForm(request.POST)
        if form.is_valid():
            form.save()
            # Ganti 'daftar_matkul' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('tahun_ajaran')
    else:
        form = TahunAjaranForm()

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Tahun Ajaran',
        'form': form,
    }
    return render(request, 'tambah_tahunajaran.html', context)
