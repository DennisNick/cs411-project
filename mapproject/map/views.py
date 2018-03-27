# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import loader

from .getArticles import getArticles

# Create your views here.

""" Index page, basic html is being rendered for the time being """
#def index(request):
#    return render(request, 'index.html')

def index(request):
    article_list = getArticles()
    print("HERE")
    latest_question_list = article_list
    print("is latest")
    print (latest_question_list)
    template = loader.get_template('map/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    return HttpResponse(template.render(context, request))
