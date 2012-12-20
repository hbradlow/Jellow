from django.db import models
from django.contrib import admin
from django_extensions.db.fields import *
import json

class Article(models.Model):
    pub_date = models.DateTimeField()
admin.site.register(Article)
class Paragraph(models.Model):
    article = models.ForeignKey(Article)
    text = models.TextField()
admin.site.register(Paragraph)




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
