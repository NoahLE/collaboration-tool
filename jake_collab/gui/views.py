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


def profile_public(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/profile-public.html', context)


def profile_private(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/profile-private.html', context)


def kanban(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/kanban.html', context)


def kanban_selected(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/kanban-selected.html', context)


def kanban_edit(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/kanban-edit.html', context)


def chat_single(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/chat-single.html', context)


def chat_multiple(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/chat-multiple.html', context)

def calendar(request):
    context = {
        'show_navbar': True
    }
    return render(request, 'gui/calendar.html', context)
