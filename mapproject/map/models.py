# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
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

""" Article Model
    -------------
    This is the primary model for the website, where articles
    queried from the NYTimes API are properly split up into
    fields relevant for the website.
    Title, locatoin and URL are self-explanatory.
    The synopsis is an abstract extracted from the API call
    Lat and Lon represent the latitude and longitude of the
        article's location, respectively
"""
class Article(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    url = models.URLField(blank=False)
    synopsis = models.CharField(blank=True, max_length=1000)
    lat = models.FloatField(default=0.0)
    lon = models.FloatField(default=0.0)

    class Meta:
        ordering = ['title', 'location', 'url']

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.title, self.location, self.url)

""" Collections Model
    -----------------
    A model specified for user collections, where a ManyToMany field
    designates a number of articles for a specific user collection.
"""
class Collections(models.Model):
    name = models.CharField(max_length=10)
    articles = models.ManyToManyField(Article, blank=True)

    def __str(self):
        return self.name

