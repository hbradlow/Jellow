from django.conf.urls import patterns, include, url
from django.views.generic.detail import DetailView
from collect_data.models import *

urlpatterns = patterns('collect_data.views',
     url(r'^heatmap/$', "heatmap"),
     url(r'^article/(?P<pk>[-_\w\d]+)/$', DetailView.as_view(model=Article), name='article_detail'),
)
