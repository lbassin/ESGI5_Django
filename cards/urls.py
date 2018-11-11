from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'decks/edit/(?P<id>\d+)', views.deck_edit, name='decks_edit'),
    url('decks/new', views.deck_new, name='decks_new'),
    url('decks', views.decks, name='decks'),
    url('', views.cards, name='cards'),
]
