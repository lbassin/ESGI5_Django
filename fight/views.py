import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.utils.safestring import mark_safe

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
