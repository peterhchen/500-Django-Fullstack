from django.urls import path
from django.conf.urls import url
from . import views

# '$' means end of string. put nothing here.
urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]