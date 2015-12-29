__author__ = 'Alex'


from django.conf.urls import include, url


urlpatterns = [
    url(r'^result/$', 'search.views.ajax_search'),
    url(r'^', 'search.views.basic')]

