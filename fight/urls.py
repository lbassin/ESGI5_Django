from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='fight_index'),
    url(r'^bot/$', views.bot, name='fight_bot'),
    url(r'^(?P<fight_id>[^/]+)/$', views.room, name='fight_room'),
]
