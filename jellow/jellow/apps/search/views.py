from collect_data.models import Tweet
from django.shortcuts import *

def home(request):
    return render_to_response("search/home.html")
