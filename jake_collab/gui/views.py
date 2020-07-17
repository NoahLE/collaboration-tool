from django.shortcuts import render


def index(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/index.html', context)


def login(request):
    context = {
        'show_navbar': False
    }
    return render(request, 'gui/login.html', context)
