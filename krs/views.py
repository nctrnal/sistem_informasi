<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect


def krs(request):
    
    context = {
        'title': 'KRS',
    }
    return render(request, 'krs.html', context)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> e44767ec837788c4ef383bfceb6177d8c04b4d7c
