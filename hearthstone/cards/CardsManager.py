import requests
from pprint import pprint

class CardsManager:

    def __init__(self):
        self.importCards()

    def importCards(self):
        response = requests.get('https://api.hearthstonejson.com/v1/25770/frFR/cards.json')

        pprint(response)