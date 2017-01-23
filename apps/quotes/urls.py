from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.quote, name = 'add'),
    url(r'^about$', views.about, name = 'about'),
    url(r'^dash$', views.dash, name = 'dash'),
    url(r'^(?P<id>\d+)/favorite$', views.favorite, name = 'favorite'),
    url(r'^(?P<id>\d+)/delete$', views.delete, name = 'delete'),
    url(r'^(?P<id>\d+)/users$', views.users, name = 'users'),
]
