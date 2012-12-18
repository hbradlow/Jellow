import tweepy
import json

consumer_key = "LbvM0OkYPg7XlL9RkofjQ"
consumer_secret = "IS3v3Y1utG9IXThRwKj2v57aAdVGKe4d4v8mIBFmzs"

access_token = "369914853-NLK8NQ2qAjWKFhsHIWX4V3mPpKQcpQi0wO0Qn5J5"
access_token_secret = "GfwtHEeNPuL90wVMNwJXzAU7dRuarDVkDskfYadMI"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class JStreamer(tweepy.StreamListener):
    def on_data(self,data):
        tweet = json.loads(data)
        try:
            if tweet['coordinates']:
                print tweet['coordinates']
        except Exception as e:
            print e
            print tweet
            exit()

j = JStreamer()
s = tweepy.Stream(auth=auth, listener=j)
s.filter(track=['guns'],async=False,locations=[-122.75,36.8,-121.75,37.8])
