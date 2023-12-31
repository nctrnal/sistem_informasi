from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from krs.models import KRS, MataKuliah # Import model KRS
from .models import Nilai  # Import model Nilai
from .forms import NilaiForm

def daftar_krs(request):
    krs_perlu_dinilai = KRS.objects.filter(status='disetujui', nilai__isnull=True)
    
    context = {
        'title': 'Daftar KRS Perlu Dinilai',
        'krs_perlu_dinilai': krs_perlu_dinilai,
    }
    return render(request, 'daftar.html', context)

def input_nilai(request, krs_id):
    krs = get_object_or_404(KRS, id=krs_id)
    mata_kuliah_list = krs.mata_kuliah.split(',')

    if request.method == 'POST':
        nilai_list = []
        for mata_kuliah in mata_kuliah_list:
            nilai = request.POST.get(mata_kuliah)
            nilai_list.append(nilai)
        
        nilai_str = ",".join(nilai_list)
        krs.nilai = nilai_str
        krs.save()
        return redirect('daftar_krs')  # Ganti 'krs_list' dengan nama URL yang sesuai
    
    nilai_formset = []
    for mata_kuliah in mata_kuliah_list:
        nilai_formset.append({'mata_kuliah': mata_kuliah})
    
    return render(request, 'input_nilai.html', {'krs': krs, 'nilai_formset': nilai_formset})






