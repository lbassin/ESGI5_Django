from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

rooms = []


class WaitingConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.room_group_name = 'waiting'

    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        for room in rooms:
            self.new_room(room)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        rooms.append(text_data_json)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'new_room',
                'id': text_data_json['id'],
                'user': text_data_json['user'],
                'victory': text_data_json['victory'],
                'defeat': text_data_json['defeat'],
                'deck': text_data_json['deck']
            }
        )

    def new_room(self, event):
        self.send(text_data=json.dumps({
            'id': event['id'],
            'user': event['user'],
            'victory': event['victory'],
            'defeat': event['defeat'],
            'deck': event['deck'],
            'action': 'add'
        }))

    def remove_room(self, event):
        for data in rooms:
            if data['id'] == event['id']:
                rooms.remove(data)
                break

        self.send(text_data=json.dumps({
            'id': event['id'],
            'action': 'remove'
        }))
