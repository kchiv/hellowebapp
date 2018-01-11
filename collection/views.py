# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template.defaultfilters import slugify
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

def create_profile(request):
	form_class = ProfileForm

	if request.method == 'POST':
		# get data from form
		form = form_class(request.POST)
		if form.is_valid():
			# check if form is valid but don't save
			# instance yet
			profile = form.save(commit=False)

			# set additional details
			profile.user = request.user
			profile.slug = slugify(profile.name)

			# save the object
			profile.save()

			# redirect to newly created profile
			return redirect('profile_detail', slug=profile.slug)
	# otherwise create the form
	else:
		form = form_class()
	return redirect(request, 'collection/create_profile.html', {'form': form,})
