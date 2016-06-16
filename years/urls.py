from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_years, name='years'),
    url(r'^year/(?P<pk>[0-9]+)/$', views.year_detail, name='detail'),
    url(r'^year/new', views.new_year, name='new_year')
]
