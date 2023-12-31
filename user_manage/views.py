from django.shortcuts import render, redirect, get_object_or_404
from authentication.models import CustomUser
from user_manage.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib import messages
from django.http import HttpResponseForbidden
import logging


@login_required(login_url='authentication:login')
# @permission_required('Akademik')
# def akademik(request):
#     user = request.user
#     return user.role == 'Akademik'

# @user_passes_test(akademik)
def user_list(request):
    users = CustomUser.objects.all()  # Use CustomUser instead of User
    context = {
        'users': users,
        'title' : 'Admin'
        }
    return render(request, 'user_list.html', context)

def add_user(request):
    # custom_user = CustomUser.objects.get(username=request.user.username)
    # if custom_user.role != 'akademik':
    #     return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini")

    logger = logging.getLogger(__name__)
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
        else:
            logger.error('Form tidak valid: %s', form.errors)
    else:
        form = UserCreationForm()
    
    context = {
        'form': form,
        'title': 'Admin'
        }
    return render(request, 'add_user.html', context)

def hapus_user(request, pk):
    # custom_user = CustomUser.objects.get(username=request.user.username)
    # if custom_user.role != 'akademik':
    #     return HttpResponseForbidden("Anda tidak memiliki izin untuk mengakses halaman ini")
    
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        messages.success(
            request, f'User "{user.username}" berhasil dihapus.')
        return redirect('user-list')  # Redirect to the 'daftar_matkul' view

    return render(request, 'hapus_user_confirm.html', {'user_list': user})

