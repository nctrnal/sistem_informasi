from django.shortcuts import render

def dosenwali(request):
    context = {
        'title' : 'Dosen Wali'
    }
    return render(request, 'dosenwali.html', context)