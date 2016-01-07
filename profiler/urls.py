__author__ = 'Alex'


from django.conf.urls import include, url


urlpatterns = [
    url(r'^add_comment/$', 'profiler.views.add_comment'),
    url(r'^(\d+)/$', 'profiler.views.basic')]

