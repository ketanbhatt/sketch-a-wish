from django.conf.urls import patterns, url
from saw import views

urlpatterns = patterns('',
                       url(r'^$', views.sketchawish, name='sketchawish'),
            )
