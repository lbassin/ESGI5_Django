from django.conf.urls import url

from . import views

urlpatterns = [
    url('buy', views.buy, name='store_buy'),
    url('', views.store, name='store'),
]
