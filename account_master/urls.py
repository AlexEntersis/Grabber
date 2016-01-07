__author__ = 'Alex'


from django.conf.urls import include, url
from django.contrib.auth.views import password_reset


urlpatterns = [
    url(r'^login/$', 'account_master.views.login'),
    url(r'^logout/$', 'account_master.views.logout'),
    url(r'^my_account/$', 'account_master.views.general'),
    url(r'^reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect' : '/reset/done/'},
        name="password_reset"),
    url(r'^reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^done/$',
        'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]