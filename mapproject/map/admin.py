# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import USMap, Collections, Article

""" Registering the Map Model """
@admin.register(USMap)
class USMapAdmin(admin.ModelAdmin):
    model = USMap

@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    model = Collections

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    model = Article

