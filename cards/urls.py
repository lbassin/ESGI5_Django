from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'decks/edit/(?P<id>\d+)', views.deck_edit, name='decks_edit'),
    url(r'decks/view/(?P<id>\d+)', views.deck_view, name='decks_view'),
    url('decks/new', views.deck_new, name='decks_new'),
    url('decks', views.decks, name='decks'),
    url(r'view/(?P<id>\d+)', views.cards_view, name='cards_view'),
    url('', views.cards, name='cards'),
]
