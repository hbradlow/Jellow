from django.conf.urls import patterns, include, url

urlpatterns = patterns('search.views',
     url(r'^search/$', "home", name="home"),
     url(r'^search/politics/$', "politics", name="politics"),
     url(r'^search/world_news/$',"world_news", name="world_news"),
     url(r'^search/technology/$',"technology", name="technology"),
     url(r'^$', "info_page", name="info_page"),
)
