from django.shortcuts import render


def wisudah(request):
    context = {
        'title': 'Wisudah dan Yudisium'
    }
    return render(request, 'wisudah.html', context)
