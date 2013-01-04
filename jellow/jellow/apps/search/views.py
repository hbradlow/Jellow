from collect_data.models import Tweet
from django.shortcuts import *
from django.shortcuts import get_object_or_404


from haystack.query import SearchQuerySet

def home(request):
    paragraphs = []
    if "q" in request.GET:
        sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))
        paragraphs = [a.object for a in sqs[0:10]]
    return render_to_response("search/home.html",{"paragraphs":paragraphs},context_instance=RequestContext(request))

def info_page(request):
    return render_to_response("info_page.html",)
