#django
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

#standard
import math

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=500,null=True)
    image = models.ImageField(upload_to="user_images",null=True)

    def get_reliability_rating(self):
        """
            TODO: document
        """
        num_of_articles = len(self.Article.objects.all())
        total_article_rating = 0
        for i in num_of_articles:
            article_rating = self.Article.objects.get(id=i).Rating.overall_rating
            total_article_rating = total_article_rating + article_rating
        reliability_rating = total_article_rating / num_of_articles
        return reliability_rating
    reliability_rating = property(get_reliability_rating)

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    """
        Creates a UserProfile model for each User that is created.
    """
    if created:
        up = UserProfile.objects.create(user=instance)
admin.site.register(UserProfile)
