from django.shortcuts import render


def mahasiswa(request):
    context = {
        'title': 'Mahasiswa'
    }
    return render(request, 'mahasiswa.html', context)
