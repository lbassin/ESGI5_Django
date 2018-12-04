from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'new', views.create, name='forum_create'),
    url(r'view/(?P<id>\d+)', views.view, name='forum_view'),
    url('', views.index, name='forum_index')
]
