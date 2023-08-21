from django import forms
from .models import Mahasiswa
from dosen_pengajar.models import DosenPengajarModel
from angkatan.models import Angkatan


class MahasiswaForm(forms.ModelForm):
    doswal = forms.ModelChoiceField(queryset=DosenPengajarModel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    angkatan = forms.ModelChoiceField(queryset=Angkatan.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Mahasiswa
        fields = ['nim', 'foto', 'nama', 'tempat_lahir', 'tanggal_lahir',
                  'angkatan', 'semester', 'jk', 'agama', 'beasiswa', 'doswal', 'status']
        widgets = {
            'nim': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nim'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'required': 'false'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama'}),
            'jk': forms.RadioSelect(attrs={'type': 'radio', 'id': 'jk'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control', 'id': 'tempat_lahir'}),
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'tanggal_lahir'}),
            # 'doswal': forms.ModelChoiceField(queryset=DosenPengajarModel.objects.all()),
            'status': forms.RadioSelect(attrs={'type': 'radio', 'id': 'status'}),
            #'angkatan': forms.ModelChoiceField(attrs={'class': 'form-control', 'id': 'angkatan'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control', 'id': 'semester'}),
            'agama': forms.TextInput(attrs={'class': 'form-control', 'id': 'agama'}),
            'beasiswa': forms.TextInput(attrs={'class': 'form-control', 'id': 'beasiswa'}),
        }


def __init__(self, *args, **kwargs):
    super(MahasiswaForm, self).__init__(*args, **kwargs)
    self.fields['foto'].required = False