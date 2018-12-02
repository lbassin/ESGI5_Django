from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'new/(?P<id>\d+)', views.trade, name='trade_trade'),
    url(r'view/(?P<id>\d+)', views.view, name='trade_view'),
    url(r'', views.index, name='trade_index'),
]
