import requests
from pprint import pprint
#curl --get --include 'https://omgvamp-hearthstone-v1.p.mashape.com/cards' \
#  -H 'X-Mashape-Key: Z6pDo19Qp5mshhwlmdkNbqGL3Rh4p1007mrjsnEiPAlaAg6Sf8'
def importCards():
    url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards'
    headers = {'X-Mashape-Key' : 'Z6pDo19Qp5mshhwlmdkNbqGL3Rh4p1007mrjsnEiPAlaAg6Sf8'}
    response = requests.get(url, headers=headers)

    return response