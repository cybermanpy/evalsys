from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url(r'^$', views.authentication, name='authentication'),
    url(r'^dashboard/$', views.home, name="home"),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout')
]