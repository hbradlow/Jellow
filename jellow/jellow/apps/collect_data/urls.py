from django.conf.urls import patterns, include, url

urlpatterns = patterns('collect_data.views',
     url(r'^heatmap/$', "heatmap"),
)
