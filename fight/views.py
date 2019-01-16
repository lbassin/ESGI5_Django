import json
import random

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.utils.safestring import mark_safe

from cards.models import Card
from hearthstone.settings import CARDS_BY_DECK
from users.models import Profile


@login_required()
def index(request):
    decks = Profile.objects.get_decks(request.user)

    return render(request, 'fight/index.html', {'decks': decks})


@login_required()
def room(request, fight_id):
    decks = Profile.objects.get_decks(request.user)

    if decks.filter(id=request.GET['deck']).count() <= 0:
        return HttpResponseForbidden()

    return render(request, 'fight/room.html', {
        'fight_json': mark_safe(json.dumps({
            'room_id': fight_id,
            'deck_id': request.GET['deck']
        }))
    })


@login_required()
def bot(request):
    decks = Profile.objects.get_decks(request.user)

    if decks.filter(id=request.GET['deck']).count() <= 0:
        return HttpResponseForbidden()

    output_cards = []
    cards = decks.get(id=request.GET['deck']).cards.all()
    for card in json.loads(serializers.serialize('json', cards)):
        output_cards.append(card['fields'])

    cards = list(Card.objects.all())
    bot_cards = []
    for i in range(CARDS_BY_DECK):
        bot_cards.append(random.choice(cards))

    output_bot = []
    for card in json.loads(serializers.serialize('json', bot_cards)):
        output_bot.append(card['fields'])

    return render(request, 'fight/bot.html', {
        'cards': mark_safe(json.dumps(output_cards)),
        'bot': mark_safe(json.dumps(output_bot))
    })
