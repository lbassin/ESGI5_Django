from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url(r'', include('django.contrib.auth.urls')),
    url(r'register', views.register, name='register'),
    url(r'dashboard', views.dashboard, name='users_dashboard'),
    url(r'unfollow', views.unfollow, name='users_unfollow'),
    url(r'follow', views.follow, name='users_follow'),
    url(r'(?P<id>\d+)', views.cards, name='users_cards'),
    url(r'', views.users, name='users_list')
]
