from django import forms
from .models import MataKuliah
from dosen_pengajar.models import DosenPengajarModel

class MataKuliahForm(forms.ModelForm):
    class Meta:
        model = MataKuliah
        fields = ['kode_mata_kuliah', 'nama_mata_kuliah', 'jumlah_sks', 'program_studi', 'kelas', 'nama_pengajar']
        widgets = {
            'kode_mata_kuliah': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_mata_kuliah': forms.Select(attrs={'class': 'form-control'}),
            'jumlah_sks': forms.NumberInput(attrs={'class': 'form-control'}),
            'program_studi': forms.TextInput(attrs={'class': 'form-control'}),
            'kelas': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_pengajar': forms.Select(attrs={'class': 'form-control'}),
        }
