from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nim = form.cleaned_data.get('username')  # Mengambil NIM dari input username
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=nim, password=password)  # Menggunakan NIM sebagai username
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Ganti 'dashboard' dengan URL yang sesuai
    else:
        form = AuthenticationForm()
    
    context = {
        'title': 'Login',
        'form': form
    }
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('authentication:login')  # Ganti 'login' dengan URL halaman login Anda
