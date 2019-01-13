from django.conf.urls import url

from fight.consumers.fight import FightConsumer
from fight.consumers.waiting import WaitingConsumer

websocket_urlpatterns = [
    url(r'^ws/fight/(?P<fight_id>[^/]+)/$', FightConsumer),
    url(r'^ws/waiting/$', WaitingConsumer),
]
