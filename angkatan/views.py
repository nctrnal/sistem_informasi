from django.shortcuts import render

def angkatan(request):
    context = {
        'title' : 'Angkatan'
    }
    return render(request, 'angkatan.html', context)
