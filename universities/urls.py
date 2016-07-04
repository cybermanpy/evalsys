from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dashboard/universities', views.view_universities, name='universities'),
    # url(r'^dashboard/university/(?P<pk>[0-9]+)/$', views.university_detail, name='detail'),
    url(r'^dashboard/university/new', views.new_university, name='new_university')
]
