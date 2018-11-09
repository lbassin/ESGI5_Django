from django.http import HttpResponse
from . import CardsManager as manager
from pprint import pprint

def index(request):
    data = manager.importCards().json()

    for key, elem in enumerate(data):
        pprint(key)
        pprint(elem)
    response = HttpResponse(data)
    response['Content-Type'] = 'application/json'
    return response
