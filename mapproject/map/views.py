# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView
from .models import Collections

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

    # Your code
    if request.method == 'GET':  # If the form is submitted

        search_query = request.GET.get('search_box', None)
        print('this is search query')
        print(search_query)
        for article in article_list:
            print(article[1][0])
            if (article[1][0] == search_query):
                print("got one")
                search_query = article
                break

        # Do whatever you need with the word the user looked for
        context = {'article_list': article_list, 'search_result': search_query}

    return HttpResponse(template.render(context, request))

def userpage(request):
    template = loader.get_template('map/userpage.html')
    collections = None
    context = { 'collections': collections }
    return HttpResponse(template.render(context, request))


