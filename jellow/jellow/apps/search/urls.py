from django.conf.urls import patterns, include, url

urlpatterns = patterns('search.views',
     url(r'^search/$', "home", name="home"),
     url(r'^$', "info_page", name="info_page"),
     url(r'^$',"search",name="search"),
)
