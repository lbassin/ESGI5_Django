import requests, json
from pprint import pprint
from cards.models import Card

def importCards():
    url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards?locale=frFR'
    headers = {'X-Mashape-Key' : 'Z6pDo19Qp5mshhwlmdkNbqGL3Rh4p1007mrjsnEiPAlaAg6Sf8'}
    response = requests.get(url, headers=headers)
    responseJson = response.json()
    for types in responseJson:
        pprint(types)
        for elem in responseJson[types]:
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
    return response