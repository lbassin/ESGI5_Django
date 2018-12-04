from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'new/(?P<id>\d+)', views.trade, name='trade_trade'),
    url(r'view/(?P<id>\d+)', views.view, name='trade_view'),
    url(r'accept/(?P<id>\d+)', views.accept, name='trade_accept'),
    url(r'decline/(?P<id>\d+)', views.decline, name='trade_decline'),
    url('', views.index, name='trade_index'),
]
