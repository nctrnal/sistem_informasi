# forms.py di app nilai
from django import forms
from .models import Nilai

class NilaiForm(forms.ModelForm):
    class Meta:
        model = Nilai
        fields = ['nilai']
