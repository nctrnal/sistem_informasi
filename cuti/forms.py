from django import forms
from django.core.validators import FileExtensionValidator
from .models import CutiModel


class CutiForm(forms.ModelForm):
    syarat_cuti = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])]
    )
    class Meta:
        model = CutiModel
        fields = ['nama', 'tanggal_mulai', 'lama_cuti', 'syarat_cuti', 'keterangan', 'status_cuti']
        widgets = {
            'nama' : forms.HiddenInput(),
            'tanggal_mulai' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'tanggal_mulai'}),
            'lama_cuti' : forms.TextInput(attrs={'class':'form-control', 'id':'lama_cuti'}),
            'keterangan' : forms.TextInput(attrs={'class':'form-control', 'id':'lama_cuti'}),
            'status_cuti' : forms.Select(attrs={'class':'form-control', 'id':'lama_cuti'}),
            'syarat_cuti' : forms.ClearableFileInput(attrs={'accept': '.pdf', 'class': 'form-control'})
        }
        validators = [FileExtensionValidator(allowed_extensions=['application/pdf'])]