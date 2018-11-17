from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'^users/', include('django.contrib.auth.urls')),
    url('users/register', views.register, name='register'),
    url('dashboard', views.dashboard, name='users_dashboard'),
    url(r'users/(?P<id>\d+)', views.cards, name='users_cards'),
    url('users', views.users, name='users_list'),
]
