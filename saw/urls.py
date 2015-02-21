from django.conf.urls import patterns, url
from saw import views

urlpatterns = patterns('',
                       url(r'^$', views.sketchawish, name='sketchawish'),
                       url(r'^get_started/$', views.get_started, name='get_started'),
                       url(r'^start/$', views.start, name='start'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^add_wish/$', views.add_wish, name='add_wish'),
                       url(r'^get_wish/$', views.get_wish, name='get_wish'),
                       url(r'^add_sketch/$', views.add_sketch, name='add_sketch')
            )
