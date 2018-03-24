# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import USMap

# Register your models here.

""" Registering the Map Model """
@admin.register(USMap)
class USMapAdmin(admin.ModelAdmin):
    model = USMap
