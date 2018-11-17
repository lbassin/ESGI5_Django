from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'cards/decks/edit/(?P<id>\d+)', views.deck_edit, name='decks_edit'),
    url(r'cards/decks/view/(?P<id>\d+)', views.deck_view, name='decks_view'),
    url(r'cards/decks/new', views.deck_new, name='decks_new'),
    url(r'cards/decks', views.decks, name='decks'),
    url(r'cards/sell', views.cards_sell, name='cards_sell'),
    url(r'cards/view/(?P<id>\d+)', views.cards_view, name='cards_view'),
    url(r'cards', views.cards, name='cards')
]
