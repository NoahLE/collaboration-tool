from django.urls import path

from . import views

# URL prefix is /gui/
urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('alerts/', views.alerts, name='alerts'),
    path('wiki-main/', views.wiki_main, name='wiki-main'),
    path('wiki-article/', views.wiki_article, name='wiki-article'),
    path('profile/public/', views.profile_public, name='profile-public'),
    path('profile/private/', views.profile_private, name='profile-private'),
    path('kanban/selected/', views.kanban, name='kanban-view'),
    path('kanban/edit/', views.kanban_edit, name='kanban-edit'),
    path('kanban/selected/', views.kanban_selected, name='kanban-submitted'),
    path('kanban/', views.kanban, name='kanban'),
    path('', views.login),
    # path('gui/wiki', views.wiki),
    # path('gui/article', views.article),
    # path('gui/kanban', views.kanban),
    # path('gui/profile-public', views.profile_public),
    # path('gui/profile-private', views.profile_private),
    # path('gui/walkthrough', views.walkthrough),
    # path('gui/settings', views.settings),
    # path('gui/notifications', views.notifications),
    # path('gui/messaging', views.messaging),
    # path('gui/calendar', views.calendar),
    # path('gui/chat-room', views.chat_room)
    # path('gui/login', views.login),
    # path('gui/login', views.login),
    # path('gui/login', views.login),
    # path('gui/login', views.login),
    # path('gui/login', views.login),
    # path('gui/login', views.login),
    # path('gui/login', views.login)
]