# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def frontend(request):
	context = {}
	template = 'frontend.html'
	return render(request,template,context)

def backend(request):
	context = {}
	template = 'backend.html'
	return render(request,template,context)

def backend_battleship(request):
	context = {}
	template = 'backend_battleship.html'
	return render(request,template,context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)