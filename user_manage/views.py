from django.shortcuts import render, redirect
from authentication.models import CustomUser
from user_manage.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# @login_required(login_url='authentication:login')

def user_list(request):
    users = CustomUser.objects.all()  # Use CustomUser instead of User
    context = {'users': users}
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

