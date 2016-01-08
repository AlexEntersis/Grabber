__author__ = 'Alex'


from django.conf.urls import include, url


urlpatterns = [
    url(r'^(\d+)/$', 'profiler.views.basic'),
    url(r'^(\d+)/all_comments/$', 'profiler.views.all_comments'),
    url(r'^(\d+)/add_comment/$', 'profiler.views.add_comment')
]

