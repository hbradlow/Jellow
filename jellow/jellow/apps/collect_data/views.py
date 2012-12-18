from collect_data.models import Tweet
from django.shortcuts import *

def heatmap(request):
    tweets = Tweet.objects.all()
    coordinates = []
    for t in tweets:
        for coord in t.coordinate_set.all():
            coordinates.append(coord)
    return render_to_response("collect_data/heatmap.html",{"coordinates":coordinates})
