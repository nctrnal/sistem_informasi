from django import forms
from .models import DosenWaliModel


class DosenWaliForm(forms.ModelForm):
    class Meta:
        model = DosenWaliModel
        fields = ['nrp', 'nama_doswal', 'jk', 'prodi', 'kelas']
        widgets = {
            'nrp': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nim'}),
            'nama_doswal': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama'}),
            'jk': forms.RadioSelect(attrs={'type': 'radio', 'id': 'jk'}),
            'prodi': forms.TextInput(attrs={'class': 'form-control', 'id': 'prodi'}),
            'kelas': forms.TextInput(attrs={'class': 'form-control', 'id': 'kelas'}),
        }
