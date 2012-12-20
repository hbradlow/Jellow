from collect_data.models import Tweet
from django.shortcuts import *
from search.models import Article

def home(request):
    return render_to_response("search/home.html")
def search(request):
    articles = Article.objects.filter(Name__icontains=request.GET["q"])
    print articles
    return render_to_response("search/home.html",{"articles_list": articles})
