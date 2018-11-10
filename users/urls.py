from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^register', views.register, name='register'),
    url(r'^cards', views.cards, name='users_cards')
]
