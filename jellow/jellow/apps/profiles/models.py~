from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=500)
    image = models.ImageField(upload_to="user_images")
admin.site.register(UserProfile)
