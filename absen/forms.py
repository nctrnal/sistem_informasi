from django import forms
from .models import Absen
from mahasiswa.models import Mahasiswa
from dosen_pengajar.models import DosenPengajarModel
from matakuliah.models import MataKuliah
from django.forms import formset_factory


class AbsenForm(forms.ModelForm):
    pilihan_kehadiran = {
        ('Hadir', 'Hadir'),
        ('Tidak Hadir', 'Tidak Hadir'),
        ('Izin', 'Izin'),
    }
    dosen = forms.ModelChoiceField(queryset=DosenPengajarModel.objects.all(),
                                   widget=forms.HiddenInput()) 

    kehadiran = forms.ChoiceField(choices=pilihan_kehadiran)
    mahasiswa = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))
    mata_kuliah = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = Absen
        fields = ['dosen', 'mahasiswa', 'kehadiran', 'mata_kuliah']
