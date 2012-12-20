from collect_data.models import Tweet
from django.shortcuts import *
from search.models import Article

from haystack.query import SearchQuerySet

def home(request):
    paragraphs = []
    if "q" in request.GET:
        sqs = SearchQuerySet().filter(content_auto=request.GET.get('q', ''))
        paragraphs = [a.object for a in sqs[0:10]]
    return render_to_response("search/home.html",{"paragraphs":paragraphs})

