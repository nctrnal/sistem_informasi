from django.shortcuts import render


def pengajar(request):
    context = {
        'title': 'Dosen Pengajar'
    }
    return render(request, 'pengajar.html', context)
