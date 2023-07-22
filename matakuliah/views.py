from django.shortcuts import render
from .models import MataKuliah
from django.shortcuts import render, get_object_or_404, redirect

def matakuliah(request):
    context = {
        'title' : 'Matakuliah'
    }
    mata_kuliah_list = MataKuliah.objects.all()
    return render(request, 'matakuliah.html', {'mata_kuliah_list': mata_kuliah_list})

def edit_mata_kuliah(request, pk):
    mata_kuliah = get_object_or_404(MataKuliah, pk=pk)

    if request.method == 'POST':
        # Proses form edit mata kuliah disini
        return redirect('daftar_mata_kuliah')

    return render(request, 'edit_mata_kuliah.html', {'mata_kuliah': mata_kuliah})

def hapus_mata_kuliah(request, pk):
    mata_kuliah = get_object_or_404(MataKuliah, pk=pk)

    if request.method == 'POST':
        # Proses penghapusan mata kuliah disini
        return redirect('daftar_mata_kuliah')

    return render(request, 'hapus_mata_kuliah.html', {'mata_kuliah': mata_kuliah})

def tambah_mata_kuliah(request):
    if request.method == 'POST':
        # Proses form tambah mata kuliah disini
        return redirect('daftar_mata_kuliah')

    return render(request, 'tambah_mata_kuliah.html')
