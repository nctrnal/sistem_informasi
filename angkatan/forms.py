from django import forms
from .models import Angkatan

class AngkatanForm(forms.ModelForm):
    class Meta:
        model = Angkatan
        fields = ['nama_angkatan', 'kurikulum']
        widgets = {
            'nama_angkatan': forms.TextInput(attrs={'class': 'form-control'}),
            'kurikulum': forms.TextInput(attrs={'class': 'form-control'}),
        }