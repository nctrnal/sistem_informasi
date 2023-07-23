from django import forms
from .models import Mahasiswa


class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nim', 'foto', 'nama', 'tempat_lahir', 'tanggal_lahir',
                  'angkatan', 'semester', 'jk', 'agama', 'beasiswa']
        widgets = {
            'nim': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nim'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'required': 'false'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control', 'id': 'tempat_lahir'}),
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'tanggal_lahir'}),
            'angkatan': forms.NumberInput(attrs={'class': 'form-control', 'id': 'angkatan'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'id': 'semester'}),
            'jk': forms.TextInput(attrs={'class': 'form-control', 'id': 'jk'}),
            'agama': forms.TextInput(attrs={'class': 'form-control', 'id': 'agama'}),
            'beasiswa': forms.TextInput(attrs={'class': 'form-control', 'id': 'beasiswa'}),
        }


def __init__(self, *args, **kwargs):
    super(MahasiswaForm, self).__init__(*args, **kwargs)
    self.fields['foto'].required = False
