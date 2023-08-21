from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser  # Use your custom user model
        fields = UserCreationForm.Meta.fields + ('email', 'NIM', 'role','password1','username','password2')  # Sesuaikan dengan kolom yang ingin ditampilkan
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'NIM': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
