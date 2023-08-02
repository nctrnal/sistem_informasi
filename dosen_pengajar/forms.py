from django import forms
from .models import DosenPengajarModel


class DosenPengajarForm(forms.ModelForm):
    class Meta:
        model = DosenPengajarModel
        fields = ['nrp', 'foto', 'nama', 'jk', 'tempat_lahir',
                  'tanggal_lahir', 'alamat', 'email', 'status', 'prodi', 'agama', 'kelas']
        widgets = {
            'nrp': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nim'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'required': 'false'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama'}),
            'jk': forms.RadioSelect(attrs={'type': 'radio', 'id': 'jk'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control', 'id': 'tempat_lahir'}),
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'tanggal_lahir'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'id': 'alamat'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),
            'kelas': forms.TextInput(attrs={'class': 'form-control', 'id': 'kelas'}),
            'status': forms.RadioSelect(attrs={'type': 'radio', 'id': 'status'}),
            'prodi': forms.TextInput(attrs={'class': 'form-control', 'id': 'prodi'}),
            'agama': forms.TextInput(attrs={'class': 'form-control', 'id': 'agama'}),
        }

    def __init__(self, *args, **kwargs):
        super(DosenPengajarForm, self).__init__(*args, **kwargs)
        self.fields['foto'].required = False
