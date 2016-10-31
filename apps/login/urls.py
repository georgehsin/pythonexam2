from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.register, name = 'register'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^$', views.index, name = 'index'),
    url(r'^logout$', views.logout, name = 'logout'),

]