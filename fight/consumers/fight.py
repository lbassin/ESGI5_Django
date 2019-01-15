from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from django.core import serializers

from cards.models import Deck, Card
from history.models import History
from users.models import Profile


class FightConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.room_id = ''
        self.room_group_name = ''

    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['fight_id']
        self.room_group_name = 'chat_%s' % self.room_id

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'join',
                'data': {
                    'player': {
                        'id': self.scope['user'].id,
                        'name': self.scope['user'].username
                    }
                }
            }
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_send)(
            'waiting',
            {
                'type': 'remove_room',
                'id': self.room_id
            }
        )

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)

        if data['action'] == 'defeat':
            self.defeat(data)
            return

        if data['action'] == 'victory':
            self.victory(data)
            return

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': data['action'],
                'data': data['data']
            }
        )

    def join(self, event):
        self.send(text_data=json.dumps({
            'action': 'join',
            'player': event['data']['player']
        }))

    def ready(self, event):
        print(event)

        async_to_sync(self.channel_layer.group_send)(
            'waiting',
            {
                'type': 'remove_room',
                'id': self.room_id
            }
        )

        cards1 = Deck.objects.get(id=event['data']['first']['deck']).cards.all()
        player_one = {'user': event['data']['first']['id'], 'life': 3, 'cards': list()}
        for card in json.loads(serializers.serialize('json', cards1)):
            player_one['cards'].append(card['fields'])

        cards2 = Deck.objects.get(id=event['data']['second']['deck']).cards.all()
        player_two = {'user': event['data']['second']['id'], 'life': 3, 'cards': list()}
        for card in json.loads(serializers.serialize('json', cards2)):
            player_two['cards'].append(card['fields'])

        self.send(text_data=json.dumps({
            'action': 'start',
            'first': player_one,
            'second': player_two
        }))

    def play(self, event):
        attack = Card.objects.get(cardId=event['data']['card']).attack

        self.send(text_data=json.dumps({
            'action': 'play',
            'player': event['data']['player'],
            'attack': attack
        }))

    def update(self, event):
        self.send(text_data=json.dumps({
            'action': 'update',
            'player': event['data']['player'],
            'cards': event['data']['cards'],
            'life': event['data']['life']
        }))

        if event['data']['life'] <= 0:
            self.send(text_data=json.dumps({
                'action': 'end',
                'player': event['data']['player'],
                'life': 0
            }))

    def defeat(self, event):
        profile = Profile.objects.get(user_id=event['data']['player'])
        profile.defeat = profile.defeat + 1
        profile.save()

        history = History(user_id=event['data']['player'], text="Lose a fight", type="defeat")
        history.save()

    def victory(self, event):
        profile = Profile.objects.get(user_id=event['data']['player'])
        profile.victory = profile.victory + 1
        profile.save()

        history = History(user_id=event['data']['player'], text="Won a fight", type="victory")
        history.save()
