from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import CustomUser
from user_manage.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# @login_required(login_url='authentication:login')

def user_list(request):
    users = CustomUser.objects.all()  # Use CustomUser instead of User
    context = {
        'users': users,
        'title' : 'Admin'
        }
    return render(request, 'user_list.html', context)

def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserCreationForm()
    
    context = {'form': form}
    return render(request, 'add_user.html', context)

def hapus_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(
            request, f'User "{user.username}" berhasil dihapus.')
        return redirect('user-list')  # Redirect to the 'daftar_matkul' view

    return render(request, 'hapus_user_confirm.html', {'user_list': user})

