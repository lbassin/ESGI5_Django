from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url('dashboard', views.dashboard, name='dashboard'),
    url('register', views.register, name='register'),
    url('cards', views.cards, name='users_cards'),
    url('decks/new', views.decks_new, name='users_decks_new'),
    url('decks', views.decks, name='users_decks')
]
