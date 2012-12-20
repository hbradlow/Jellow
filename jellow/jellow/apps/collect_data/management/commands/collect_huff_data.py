from django.core.management.base import BaseCommand, CommandError
import requests
import json
import BeautifulSoup
from collect_data.models import *
import warnings

class Command(BaseCommand):
    def handle(self, *args, **options):
        warnings.simplefilter("ignore")
        limit = 50
        for i in range(100):
            print "Starting article " + str(i*limit)
            base_url = "http://huffpo.enterpriseapi.daylife.com/articles/syria?format=json&limit=" + str(limit*i + limit) + "&offset=" + str(limit*i)
            objects = json.loads(requests.get(base_url).text)

            for o in objects['response']['payload']['article']:
                article = Article.objects.create(pub_date=o['timestamp'],raw=json.dumps(o)) 
                article.process_raw()
                article.save()
