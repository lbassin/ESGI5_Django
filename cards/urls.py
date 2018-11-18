from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'decks/edit/(?P<id>\d+)', views.deck_edit, name='decks_edit'),
    url(r'decks/view/(?P<id>\d+)', views.deck_view, name='decks_view'),
    url(r'decks/new', views.deck_new, name='decks_new'),
    url(r'decks', views.decks, name='decks'),
    url(r'sell', views.cards_sell, name='cards_sell'),
    url(r'view/(?P<id>\d+)', views.cards_view, name='cards_view'),
    url(r'', views.cards, name='cards')
]
