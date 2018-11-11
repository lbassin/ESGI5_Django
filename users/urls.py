from django.conf.urls import url
from django.urls import include

from . import views

urlpatterns = [
    url('', include('django.contrib.auth.urls')),
    url('dashboard', views.dashboard, name='dashboard'),
    url('register', views.register, name='register')
]
