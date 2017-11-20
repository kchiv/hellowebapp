# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from collection.models import Profile

class ProfileAdmin(admin.ModelAdmin):
	model = Profile
	list_display = ('name', 'description', 'slug',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Profile, ProfileAdmin)