from django.conf.urls import include, patterns, url

urlpatterns = patterns('games.views',
    url(r'^create/$', 'create', name='create'),
    url('^(?P<game_id>\d+)/$', 'show', name='show'),
)
