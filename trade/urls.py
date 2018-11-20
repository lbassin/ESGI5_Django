from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'(?P<id>\d+)', views.trade, name='trade_trade')
]
