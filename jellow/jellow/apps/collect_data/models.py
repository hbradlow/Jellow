from django.db import models
from django.contrib import admin
from django_extensions.db.fields import *
import json
import BeautifulSoup
import requests

class Article(models.Model):
    pub_date = models.DateTimeField()
    raw = models.TextField()
    headline = models.CharField(max_length=500)
    def create_paragraphs(self,o):
        url = o['url'] 
        text = requests.get(url).text 
        soup = BeautifulSoup.BeautifulSoup(text)
        try:
            for paragraph in soup.find("div",{ "class" : "articleBody"}).findAll("p"):
                Paragraph.objects.create(article=self,text=str(paragraph))
        except AttributeError:
            pass #failed to load paragraphs
    def process_raw(self):
        o = json.loads(self.raw)

        self.create_paragraphs(o)
        self.headline = o['headline']

admin.site.register(Article)
class Paragraph(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField()
admin.site.register(Paragraph)

rating_choices = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
)
class Rating(models.Model):
    article = models.ForeignKey(Article,null=True)
    organization = models.CharField(max_length=10,choices=rating_choices)
    support = models.CharField(max_length=10,choices=rating_choices)
    readability = models.CharField(max_length=10,choices=rating_choices)
    tags = models.CharField(max_length=10,choices=rating_choices)
    comments = models.TextField()
admin.site.register(Rating)




class Tweet(models.Model):
    text = models.TextField()
    raw = models.TextField()
    created_at = CreationDateTimeField(null=True)
    def process_raw(self):
        obj = json.loads(self.raw)
        self.text = obj['text']
        if obj['coordinates']:
            coord = obj['coordinates']
            c = Coordinate()
            c.tweet = self
            c.type = coord['type']
            c.latitude = coord['coordinates'][0]
            c.longitude = coord['coordinates'][1]
            c.save()
        if obj['entities']['hashtags']:
            for htag in obj['entities']['hashtags']:
                h = Hashtag()
                h.tweet = self
                h.text = htag['text']
                h.save()
        self.save()

    def __unicode__(self):
        return "Tweet:"+self.text
admin.site.register(Tweet)

class Coordinate(models.Model):
    tweet = models.ForeignKey(Tweet)
    type = models.CharField(max_length=30)
    latitude = models.FloatField()
    longitude = models.FloatField()
admin.site.register(Coordinate)

class Hashtag(models.Model):
    tweet = models.ForeignKey(Tweet)
    text = models.CharField(max_length=200)
    def __unicode__(self):
        return self.text
admin.site.register(Hashtag)
