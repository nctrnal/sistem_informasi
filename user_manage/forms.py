from django import forms
from django.contrib.auth.forms import UserCreationForm
from authentication.models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser  # Use your custom user model
        fields = UserCreationForm.Meta.fields + ('email', 'NIM')  # Sesuaikan dengan kolom yang ingin ditampilkan
