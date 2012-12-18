from django.core.management.base import BaseCommand, CommandError
from collect_data.models import Tweet

import tweepy

consumer_key = "LbvM0OkYPg7XlL9RkofjQ"
consumer_secret = "IS3v3Y1utG9IXThRwKj2v57aAdVGKe4d4v8mIBFmzs"

access_token = "369914853-NLK8NQ2qAjWKFhsHIWX4V3mPpKQcpQi0wO0Qn5J5"
access_token_secret = "GfwtHEeNPuL90wVMNwJXzAU7dRuarDVkDskfYadMI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class JStreamer(tweepy.StreamListener):
    def on_data(self,data):
        t = Tweet.objects.create(raw=data)
        t.process_raw()
        print t

class Command(BaseCommand):

    def handle(self, *args, **options):
        j = JStreamer()
        s = tweepy.Stream(auth=auth, listener=j)
        s.filter(track=['guns'],async=False,locations=[-122.75,36.8,-121.75,37.8])
