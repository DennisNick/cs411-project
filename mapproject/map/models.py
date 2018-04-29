# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

from .getArticles import getArticles

""" Map Model
    --------
    This is the model for implementing the basic map configuration.
    Under development
"""
class USMap(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.URLField(blank=False)

    class Meta:
        ordering = ['title', 'location', 'url']

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.title, self.location, self.url)


class Sideshow(models.Model):
    title = models.CharField(max_length=100)
    published_by = models.CharField(max_length=30)
    publish_date = models.DateField('Publication date')
    article_synopsis = models.CharField(max_length=1000)
    url = models.URLField(blank=False)

    def __str__(self):
        return self.title

class Collections(models.Model):
    name = models.CharField(max_length=10)
    articles = models.ManyToManyField(Article)

    def __str(self):
        return self.name

