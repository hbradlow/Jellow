from django.core.management.base import BaseCommand, CommandError
import requests
import json
import BeautifulSoup
from collect_data.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        limit = 50
        for i in range(30):
            base_url = "http://huffpo.enterpriseapi.daylife.com/articles/syria?format=json&limit=" + str(limit*i + limit) + "&offset=" + str(limit*i)
            objects = json.loads(requests.get(base_url).text)
            for o in objects['response']['payload']['article']:
                article = Article.objects.create(pub_date=o['timestamp']) 
                url = o['url'] 
                text = requests.get(url).text 
                soup = BeautifulSoup.BeautifulSoup(text)
                try:
                    for paragraph in soup.find("div",{ "class" : "articleBody"}).findAll("p"):
                        Paragraph.objects.create(article=article,text=str(paragraph))
                except AttributeError:
                    article.delete()
