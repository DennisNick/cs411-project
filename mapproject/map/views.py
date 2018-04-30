# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from .models import Collections
from .cache import cacheArticles, create_article, cacheCollections, createCollections
from .keys import googlemaps_apikey
import json

# getArticles.py file
from .getArticles import getArticles, convert

""" Index page, basic html is being rendered for the time being
    Makes use of the getArticles function to properly obtain
    articles queried from the NYTimes API
"""
def index(request):
    article_list = cacheArticles(request)
    createCollections(request)

    template = loader.get_template('map/index.html')
    context = { 'article_list': article_list }

    # Do whatever you need with the word the user looked for
    context = {'article_list': article_list} #, 'search_result': search_query}

    return HttpResponse(template.render(context, request))

""" Login function, defined for the ease of socially logging in with a Google+ account """
@login_required
def login(request):
    login_template = loader.get_template('registration/login.html')
    return render(request, login_template)

""" Logout function, defined to logout of a Google+ account """
@login_required
def logout(request):
    logout(request)
    return redirect('login.html')

""" User page, where the user's favorited collections are located, as well as the
    ability to logout.
"""
@login_required
def userpage(request):
    user = request.user
    logout = False

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    if (user.social_auth.count != 0):
        logout = True

    collection = Collections.object.all()
    context = { 'google_login': google_login, 'logout': logout, 'collection': collection}
    return render(request, 'registration/userpage.html', context)

@login_required
def store_article(request):
    user = request.user

    if(request.method == 'POST'):
        data = convert(request.POST)
        title = data['title']
        cacheCollections(title)
    return redirect(request, 'login.html')
