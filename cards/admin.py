# Register your models here.
import random
import json
import requests
from pprint import pprint

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from cards.models import Card


def import_cards():
    url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards?locale=frFR'
    headers = {'X-Mashape-Key': 'Z6pDo19Qp5mshhwlmdkNbqGL3Rh4p1007mrjsnEiPAlaAg6Sf8'}
    response_json = requests.get(url, headers=headers).json()
    for types in response_json:
        pprint(types)
        for elem in response_json[types]:
            if bool(elem.get('img')) is False:
                continue

            card = Card.objects.create()
            if bool(elem.get('name')) is not False:
                card.name = elem['name'] if elem['name'] != "" else ""
            if bool(elem.get('cardId')) is not False:
                card.cardId = elem['cardId'] if elem['cardId'] != "" else ""
            if bool(elem.get('dbfId')) is not False:
                card.dbfId = elem['dbfId'] if elem['dbfId'] != "" else ""
            if bool(elem.get('cardSet')) is not False:
                card.cardSet = elem['cardSet'] if elem['cardSet'] != "" else ""
            if bool(elem.get('type')) is not False:
                card.type = elem['type'] if elem['type'] != "" else ""
            if bool(elem.get('text')) is not False:
                card.text = elem['text'] if elem['text'] != "" else ""
            if bool(elem.get('playerClass')) is not False:
                card.playerClass = elem['playerClass'] if elem['playerClass'] != "" else ""
            if bool(elem.get('health')) is not False:
                card.health = elem['health'] if elem['health'] != "" else ""
            if bool(elem.get('cost')) is not False:
                card.cost = elem['cost'] if elem['cost'] != "" else ""
            if bool(elem.get('attack')) is not False:
                card.attack = elem['attack'] if elem['attack'] != "" else ""
            if bool(elem.get('mechanics')) is not False:
                card.mechanics = json.dumps(elem['mechanics']) if len(elem['mechanics']) > 0 else ""
            if bool(elem.get('faction')) is not False:
                card.faction = elem['faction'] if elem['faction'] != "" else ""
            if bool(elem.get('rarity')) is not False:
                card.rarity = elem['rarity'] if elem['rarity'] != "" else ""
            if bool(elem.get('collectible')) is not False:
                card.collectible = elem['collectible'] if elem['collectible'] != "" else ""
            if bool(elem.get('img')) is not False:
                card.img = elem['img'] if elem['img'] != "" else ""
            if bool(elem.get('imgGold')) is not False:
                card.imgGold = elem['imgGold'] if elem['imgGold'] != "" else ""

            card.save()


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'isDefault')
    change_list_template = "cards/changelist.html"
    ordering = ('-isDefault',)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-api/', self.import_api),
        ]
        return my_urls + urls

    def import_api(self, request):
        if len(Card.objects.all()) <= 0:
            import_cards()

            cards = list(Card.objects.all())
            for i in range(30):
                card = random.choice(cards)
                card.isDefault = True
                card.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
