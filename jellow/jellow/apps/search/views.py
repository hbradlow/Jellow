from collect_data.models import Tweet
from django.shortcuts import *
from django.shortcuts import get_object_or_404


from haystack.query import SearchQuerySet

def home(request):
    paragraphs = []
    if "q" in request.GET:
        sqs = SearchQuerySet().filter(content=request.GET.get('q', ''))
        paragraphs = [a.object for a in sqs[0:30]]
    return render_to_response("search/home.html",{"paragraphs":paragraphs},context_instance=RequestContext(request))


def politics(request):
    paragraphs = []
    sqs = SearchQuerySet().filter(tags='Politics')
    paragraphs = [a.object for a in sqs[0:10]]
    return render_to_response("search/home.html",{"paragraphs":paragraphs},context_instance=RequestContext(request))

def world_news(request):
    paragraphs = []
    sqs= SearchQuerySet().filter(tags='World News')
    paragraphs = [a.object for a in sqs[0:10]]
    return render_to_response("search/home.html",{"paragraphs":paragraphs},context_instance=RequestContext(request))

def technology(request):
    paragraphs = []
    sqs= SearchQuerySet().filter(tags='Technology')
    paragraphs = [a.object for a in sqs[0:10]]
    return render_to_response("search/home.html",{"paragraphs":paragraphs},context_instance=RequestContext(request))

def search(request):
    return render_to_response("search/search.html",)


def info_page(request):
    return render_to_response("search/info_page.html",)
