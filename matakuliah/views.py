from .models import MataKuliah
from django.shortcuts import render, get_object_or_404, redirect
from .forms import MataKuliahForm
from django.contrib import messages
from dosen_pengajar.models import DosenPengajarModel
from django.contrib.auth.decorators import login_required


@login_required(login_url='authentication:login')


def matakuliah(request):
    jurusan = request.GET.get('jurusan', None)

    if jurusan:
        if jurusan == 'semua_jurusan':
            mata_kuliah_list = MataKuliah.objects.all()
        else:
            mata_kuliah_list = MataKuliah.objects.filter(program_studi=jurusan)
    else:
        mata_kuliah_list = MataKuliah.objects.all()

    # mata_kuliah_list = MataKuliah.objects.all()

    context = {
        'title': 'Mata Kuliah',
        'mata_kuliah_list': mata_kuliah_list
    }
    return render(request, 'matakuliah.html', context)


def edit_mata_kuliah(request, pk):
    mata_kuliah = get_object_or_404(MataKuliah, pk=pk)

    if request.method == 'POST':
        form = MataKuliahForm(request.POST, instance=mata_kuliah)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Mata kuliah "{mata_kuliah.nama_mata_kuliah}" berhasil diubah !!')
            return redirect('matakuliah')
    else:
        form = MataKuliahForm(instance=mata_kuliah)

    # Konteks untuk halaman edit_matkul.html
    context = {
        'title': 'Mata Kuliah',
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
            messages.success(request, f'Mata kuliah berhasil ditambahkan !!')
            # Ganti 'daftar_matkul' dengan nama URL untuk halaman daftar mata kuliah
            return redirect('matakuliah')
    else:
        form = MataKuliahForm()

    # Ambil semua data dosen pengajar
    dosen_pengajar_list = DosenPengajarModel.objects.all()

    # Tambahkan data dosen_pengajar_list ke dalam choices untuk dropdown "Nama Pengajar"
    form.fields['nama_pengajar'].queryset = dosen_pengajar_list

    # Konteks untuk halaman tambah_matkul.html
    context = {
        'title': 'Mata Kuliah',
        'form': form,
    }
    return render(request, 'tambah_mata_kuliah.html', context)
