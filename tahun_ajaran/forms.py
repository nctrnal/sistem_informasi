from django import forms
from .models import TahunAjaranModel


class TahunAjaranForm(forms.ModelForm):
    class Meta:
        model = TahunAjaranModel
        fields = ['tahun_ajaran', 'ajaran_semester']
        widgets = {
            'tahun_ajaran': forms.TextInput(attrs={'class': 'form-control', 'id': 'tahun_ajaran'}),
            'ajaran_semester': forms.Select(attrs={'class': 'form-control', 'id': 'ajaran_semester'}),
        }
