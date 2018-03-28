# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

# getArticles.py file
from .getArticles import getArticles

""" Index page, basic html is being rendered for the time being
    Makes use of the getArticles function to properly obtain
    articles queried from the NYTimes API
"""
def index(request):
    article_list = getArticles()
    template = loader.get_template('map/index.html')
    context = { 'article_list': article_list }

    return HttpResponse(template.render(context, request))
