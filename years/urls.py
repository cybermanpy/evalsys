from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/years', views.view_years, name='years'),
    url(r'^dashboard/year/(?P<pk>[0-9]+)/$', views.year_detail, name='detail'),
    url(r'^dashboard/year/new', views.new_year, name='new_year')
]
