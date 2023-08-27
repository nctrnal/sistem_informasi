from django import forms
from .models import KRS
from mahasiswa.models import Mahasiswa
from matakuliah.models import MataKuliah

class TambahKRSForm(forms.ModelForm):
    mata_kuliah = forms.ModelMultipleChoiceField(queryset=MataKuliah.objects.all(),
                                                widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
                                                required=True)
    mahasiswa = forms.ModelChoiceField(queryset=Mahasiswa.objects.all(),
                                       widget=forms.HiddenInput())  # Ganti widget menjadi HiddenInput
    status = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'status'}))

    class Meta:
        model = KRS
        fields = ['mata_kuliah', 'mahasiswa', 'status']

    
