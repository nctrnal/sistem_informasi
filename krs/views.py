from django.shortcuts import render, get_object_or_404, redirect


def krs(request):
    
    context = {
        'title': 'KRS',
    }
    return render(request, 'krs.html', context)