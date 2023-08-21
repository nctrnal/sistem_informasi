from django import forms
from .models import WisudahYudisiumModel


class WisudahYudisiumForm(forms.ModelForm):
    class Meta:
        model = WisudahYudisiumModel
        fields = ['nim', 'lulus_sidang', 'epdamo', 'lulus_prodi', 'lulus_keuangan',
                  'lulus_bidkerjasama', 'lulus_perpus', 'toefl']
        widgets = {
            'nim': forms.TextInput(attrs={'class': 'form-control'}),
            'lulus_sidang': forms.FileInput(attrs={'class': 'form-control'}),
            'epdamo': forms.FileInput(attrs={'class': 'form-control'}),
            'lulus_prodi': forms.FileInput(attrs={'class': 'form-control'}),
            'lulus_keuangan': forms.FileInput(attrs={'class': 'form-control'}),
            'lulus_bidkerjasama': forms.FileInput(attrs={'class': 'form-control'}),
            'lulus_perpus': forms.FileInput(attrs={'class': 'form-control'}),
            'toefl': forms.FileInput(attrs={'class': 'form-control'}),
        }
