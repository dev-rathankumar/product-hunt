from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'products/home.html')


def rathan(request):
    return render(request, 'products/rathan.html')


def login(request):
    return render(request, 'products/login.html')

