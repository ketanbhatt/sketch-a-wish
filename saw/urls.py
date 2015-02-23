from django.conf.urls import patterns, url
from saw import views

urlpatterns = patterns('',
                       url(r'^$', views.sketchawish, name='sketchawish'),
                       url(r'^get_started/$', views.get_started, name='get_started'),
                       url(r'^start/$', views.start, name='start'),
                       url(r'^logout/$', views.user_logout, name='logout'),
            )
