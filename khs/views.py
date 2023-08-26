from django.shortcuts import render, get_object_or_404, redirect


def khs(request):
    
    context = {
        'title': 'KHS',
    }
    return render(request, 'khs.html', context)
