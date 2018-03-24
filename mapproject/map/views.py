# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from .models import USMap

# Create your views here.

""" Index page, basic html is being rendered for the time being """
def index(request):
    return render(request, 'index.html')
