from django import forms
from .models import Mahasiswa
from dosen_pengajar.models import DosenPengajarModel
from angkatan.models import Angkatan


class MahasiswaForm(forms.ModelForm):
    doswal = forms.ModelChoiceField(queryset=DosenPengajarModel.objects.all(
    ), widget=forms.Select(attrs={'class': 'form-control', 'id': 'doswal'}))
    angkatan = forms.ChoiceField(
        choices=Angkatan.objects.values_list('nama_angkatan', 'nama_angkatan'),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'angkatan'}))
    # angkatan = forms.ModelChoiceField(
    #     queryset=Angkatan.objects.all(),
    #     widget=forms.Select(attrs={'class': 'form-control', 'id': 'angkatan'})
    #     )
    semester = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'id': 'semester', 'readonly': 'readonly'}))

    class Meta:
        model = Mahasiswa
        fields = ['nim', 'foto', 'nama', 'tempat_lahir', 'tanggal_lahir',
                  'angkatan', 'semester', 'jk', 'agama', 'beasiswa', 'doswal', 'status', 'alamat', 'email']
        widgets = {
            'nim': forms.NumberInput(attrs={'class': 'form-control', 'id': 'nim'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'required': 'false'}),
            'nama': forms.TextInput(attrs={'class': 'form-control', 'id': 'nama'}),
            'jk': forms.RadioSelect(attrs={'type': 'radio', 'id': 'jk'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control', 'id': 'tempat_lahir'}),
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'tanggal_lahir'}),
            # 'doswal': forms.ModelChoiceField(queryset=DosenPengajarModel.objects.all()),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'status'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'id': 'alamat'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email'}),
            'angkatan': forms.ModelChoiceField(queryset=Angkatan.objects.values_list('nama_angkatan', flat=True)),
            # 'semester': forms.TextInput(attrs={'class': 'form-control', 'id': 'semester'}),
            'agama': forms.Select(attrs={'class': 'form-control', 'id': 'agama'}),
            'beasiswa': forms.TextInput(attrs={'class': 'form-control', 'id': 'beasiswa'}),
        }


def __init__(self, *args, **kwargs):
    super(MahasiswaForm, self).__init__(*args, **kwargs)
    self.fields['foto'].required = False