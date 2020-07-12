from django.shortcuts import render

def index(request):
    return render(request, 'gui/login.html')

def login(request):
    return render(request, 'gui/login.html')

def home(request):
    return render(request, 'gui/login.html')