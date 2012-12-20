from collect_data.models import *
from django.shortcuts import *

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def heatmap(request):
    tweets = Tweet.objects.all()
    coordinates = []
    for t in tweets:
        for coord in t.coordinate_set.all():
            coordinates.append(coord)
    return render_to_response("collect_data/heatmap.html",{"coordinates":coordinates})

@csrf_exempt
def submit_grade(request):
    if request.method=="POST":
        r = Rating()
        r.article = get_object_or_404(Article,pk=request.POST["article_pk"])
        r.organization = request.POST["Organization"]
        r.support = request.POST["Support/Evidence"]
        r.readability = request.POST["Readability"]
        r.tags = request.POST["Appropriatness of tags"]
        r.comments = request.POST["comments"]
        r.save()
    return HttpResponse("Done")
