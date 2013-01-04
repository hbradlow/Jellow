from django.conf.urls import patterns, include, url

urlpatterns = patterns('search.views',
     url(r'^$', "home", name="home"),
     url(r'^info_page/$', "info_page", name="info_page"),
)
