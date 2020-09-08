from django.urls import path

from . import views

# URL prefix is /gui/
urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('alerts/', views.alerts, name='alerts'),
    path('chat/single/', views.chat_single, name='chat-single'),
    path('chat/multiple/', views.chat_multiple, name='chat-multiple'),
    path('wiki-main/', views.wiki_main, name='wiki-main'),
    path('wiki-article/', views.wiki_article, name='wiki-article'),
    path('profile/public/', views.profile_public, name='profile-public'),
    path('profile/private/', views.profile_private, name='profile-private'),
    path('kanban/edit/', views.kanban_edit, name='kanban-edit'),
    path('kanban/selected/', views.kanban_selected, name='kanban-selected'),
    path('kanban/', views.kanban, name='kanban'),
    path('', views.login),
]