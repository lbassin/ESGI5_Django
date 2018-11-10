from django.http import HttpResponse
from hearthstone.cards.models import Card
from . import CardsManager as manager

def index(request):
    if(len(Card.objects.all()) <=0):
        data = manager.importCards().json()
        response = HttpResponse(data)
    else:
        data = Card.objects.all()
        response = HttpResponse(data)

    response['Content-Type'] = 'application/json'
    return response
