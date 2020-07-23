from django.shortcuts import render


def login(request):
    context = {
        'show_navbar': False
    }
    return render(request, 'gui/login.html', context)


def index(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/index.html', context)


def alerts(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/alerts.html', context)


def wiki_main(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/wiki-main.html', context)


def wiki_article(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/wiki-article.html', context)

def kanban(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/kanban.html', context)
