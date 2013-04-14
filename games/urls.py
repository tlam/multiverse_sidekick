from django.conf.urls import include, patterns, url

urlpatterns = patterns('games.views',
    url(r'^create/$', 'create', name='create'),
)
