from django.db import models
from django.contrib import admin
from django_extensions.db.fields import *
from profiles.models import UserProfile
import json
import BeautifulSoup
import requests
import math

class Article(models.Model):
    pub_date = models.DateTimeField()
    raw = models.TextField()
    headline = models.CharField(max_length=500)
    reporter = models.ForeignKey(UserProfile,null=True)
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

class Tag(models.Model):
    tag = models.CharField(max_length=500)
    def __unicode__(self):
        return self.tag
admin.site.register(Tag)

class Paragraph(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    def __unicode__(self):
        return "Headline: " + self.article.headline + " Tags: " +  ', '.join([t.tag for t in self.tags.all()])
admin.site.register(Paragraph)

rating_choices = (
    (1,"1"),
    (2,"2"),
    (3,"3"),
    (4,"4"),
    (5,"5"),
)

class Rating(models.Model):
    article = models.ForeignKey(Article,null=True)
    organization = models.IntegerField(choices=rating_choices, default=1)
    support = models.IntegerField(choices=rating_choices, default=1)
    readability = models.IntegerField(choices=rating_choices, default=1)
    tags = models.IntegerField(choices=rating_choices, default=1)
    comments = models.TextField()
    def get_overall_rating(self):
        return fsum(self.organization + self.support + self.support + self.readability + self.tags)/5.0
    overall_rating = property(get_overall_rating)
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
