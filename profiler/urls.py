__author__ = 'Alex'


from django.conf.urls import include, url


urlpatterns = [
    url(r'^(\d+)/$', 'profiler.views.basic')]

