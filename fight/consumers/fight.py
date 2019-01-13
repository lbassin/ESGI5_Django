from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json


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

        self.send(text_data=json.dumps({
            'action': 'start'
        }))
