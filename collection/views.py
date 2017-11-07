# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
	# defining the variable
	number = 6
	# passing the variable to the view
	return render(request, 'collection/index.html', {'number': number})