from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import math

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=500)
    image = models.ImageField(upload_to="user_images")
    def get_reliability_rating(self):
        num_of_articles = len(self.Article.objects.all())
        total_article_rating = 0
        for i in num_of_articles:
            article_rating = self.Article.objects.get(id=i).Rating.overall_rating
            total_article_rating = total_article_rating + article_rating
        reliability_rating = total_article_rating / num_of_articles
        return reliability_rating
    reliability_rating = property(get_reliability_rating)
admin.site.register(UserProfile)
