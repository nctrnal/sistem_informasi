from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from .models import WisudahYudisiumModel
from .forms import WisudahYudisiumForm
from mahasiswa.models import Mahasiswa


def wisudah(request):
    if request.method == 'POST':
        form = WisudahYudisiumForm(request.POST, request.FILES)
        if form.is_valid():
            nim_mahasiswa = form.cleaned_data['nim']
            try:
                mahasiswa = Mahasiswa.objects.get(nim=nim_mahasiswa)
                nama_mahasiswa = mahasiswa.nama
                wisudah, created = WisudahYudisiumModel.objects.get_or_create(
                    mahasiswa=mahasiswa)
                return redirect('dashboard')
            except Mahasiswa.DoesNotExist:
                form.add_error('nim', 'Mahasiswa tidak ditemukan.')
    else:
        form = WisudahYudisiumForm()

    # Konteks untuk halaman tambah_matkul.html
    context = {
        'title': 'Wisudah dan Yudisium',
        'form': form,
    }
    return render(request, 'wisudah.html', context)
