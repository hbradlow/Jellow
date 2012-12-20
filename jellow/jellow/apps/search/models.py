from django.db import models
from django.contrib import admin
# Create your models here.

class Article (models.Model):
    Name = models.CharField(max_length=50)
    Content = models.CharField(max_length=200)

admin.site.register(Article)
