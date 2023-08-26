from django import forms
from .models import NilaiModel


class NilaiForm(forms.ModelForm):
    class Meta:
        model = NilaiModel
        fields = ['nama_mahasiswa', 'nama_pengajar', 'jk', 'semester', 'angkatan', 'nilai']
        widgets = {
            'nama_mahasiswa': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama_mahasiswa'}),
            'nama_doswal': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama_doswal'}),
            'jk': forms.TextInput(attrs={'class': 'form-control', 'id': 'jk'}),
            'semester': forms.TextInput(attrs={'class': 'form-control', 'id': 'semester'}),
            'angkatan': forms.TextInput(attrs={'class': 'form-control', 'id': 'angkatan'}),
            'nilai': forms.TextInput(attrs={'class': 'form-control', 'id': 'nilai'}),
        }
