"""rockmylight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'rockmylight.rml.views.main', name='main'),
    url(r'^jam_session/(?P<session_id>[0-9]+)/', 'rockmylight.rml.views.jam',
        name='jam'),
    url(r'^api/dj/auto/', 'rockmylight.rml.views.api_dj_auto',
        name='api_dj_auto'),
    url(r'^api/dj/(?P<session_id>[0-9]+)/$', 'rockmylight.rml.views.api_dj',
        name='api_dj'),
    url(r'^about/', 'rockmylight.rml.views.about',
        name='about'),

    url(r'^api/start_jam/(?P<session_id>[0-9]+)/$', 'rockmylight.rml.views.start_jam',
        name='start_jam'),
    url(r'^api/jam_is_playing/(?P<session_id>[0-9]+)/$', 'rockmylight.rml.views.jam_is_playing',
        name='jam_is_playing'),
    url(r'^api/stop_jam/(?P<session_id>[0-9]+)/$', 'rockmylight.rml.views.stop_jam',
        name='stop_jam'),

    url(r'^admin/', include(admin.site.urls)),
)
