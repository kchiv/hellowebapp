# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from collection.forms import ProfileForm
from collection.models import Profile

# Create your views here.

def index(request):
	profiles = Profile.objects.all()
	return render(request, 'collection/index.html', {'profiles': profiles,})

def profile_detail(request, slug):
	profile = Profile.objects.get(slug=slug)
	return render(request, 'collection/profile_detail.html', {'profile': profile,})

def edit_profile(request, slug):
	profile = Profile.objects.get(slug=slug)
	form = ProfileForm(instance=profile)

	if request.method == 'POST':
		form = ProfileForm(data=request.POST, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('profile_detail', slug=profile.slug)

	return render(request, 'collection/edit_profile.html', {'profile': profile, 'form': form,})