# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from collection.models import Profile

# Create your views here.

def index(request):
	profiles = Profile.objects.all()
	return render(request, 'collection/index.html', {'profiles': profiles,})

def profile_detail(request, slug):
	profile = Profile.objects.get(slug=slug)
	return render(request, 'collection/profile_detail.html', {'profile': profile,})