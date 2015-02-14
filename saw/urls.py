from django.conf.urls import patterns, url
from saw import views

urlpatterns = patterns('',
                       url(r'^$', views.sketchawish, name='sketchawish'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^logout/$', views.user_logout, name='logout'),
                       url(r'^add_wish/$', views.add_wish, name='add_wish'),
                       url(r'^add_sketch/$', views.add_sketch, name='add_sketch')
            )
