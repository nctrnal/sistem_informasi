from django import forms
<<<<<<< HEAD:wisudah_yudisium/forms.py
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
=======
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser  # Use your custom user model
        fields = UserCreationForm.Meta.fields + ('email', 'NIM')  # Sesuaikan dengan kolom yang ingin ditampilkan
>>>>>>> 45e0d6cbc057d977bbba61f29374edefff3ee7ea:user_manage/forms.py
