from django.conf.urls import url

from . import views

urlpatterns = [
    url('decks/new', views.decks_new, name='decks_new'),
    url('decks', views.decks, name='decks'),
    url('', views.cards, name='cards'),
]
