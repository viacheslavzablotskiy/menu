
from django.shortcuts import render

# Create your views here.


def base(request, name):
    return render(request, 'menu/home.html', {'name': name})