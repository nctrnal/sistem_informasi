from django.shortcuts import render

def absen(request):
    context = {
        'title' : 'Absen Dosen Mahasiswa'
    }
    return render(request, 'absen.html', context)