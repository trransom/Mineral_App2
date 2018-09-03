from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
import re

from .models import Mineral
from . import forms


def in_group(str):
	groups = ['silicate', 'oxide', 'sulfate', 'sulfide', 'carbonate',
				'halide', 'sulfosalt', 'phosphate', 'borate', 'organic',
				'arsenate', 'native']
	for group in groups:
		if group in str.lower():
			return True;
	return False;
	
def route(request):
	'''Reroutes to the index view.'''
	minerals=Mineral.objects.filter(name__startswith='A')
	return render(request, 'minerals/index.html', {'minerals': minerals})
	
	
def index(request, letter):
	'''Returns a list of all the minerals in the database.'''
	minerals = Mineral.objects.filter(name__startswith=letter)
	return render(request, 'minerals/index.html', {'minerals': minerals})
	
def alphabet_view(request, letter):
	'''
	Returns a list of all the minerals beginning with 
	a specified letter.
	'''
	minerals = Mineral.objects.filter(name__startswith=letter)
	return render(request, 'minerals/index.html', {'minerals': minerals})
	
def detail(request, pk):
	'''Returns a detailed view of a single mineral.'''
	mineral = get_object_or_404(Mineral, pk=pk)
	return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
	
def search_results(request):
	'''Returns a listing of minerals matching the search.'''
	query = request.GET.get('q')
	if query:
		minerals = Mineral.objects.filter(name__icontains=query)
		return render(request, 'minerals/index.html', {'minerals': minerals})
	else:
		minerals = []
		return render(request, 'minerals/index.html', {'minerals': minerals})
		
def group_view(request, group):
	'''Returns a listing of minerals matching the given group.'''
	if group != 'other':
		minerals = Mineral.objects.filter(category__icontains=group)
		return render(request, 'minerals/index.html', {'minerals': minerals})
	else:
		minerallist = Mineral.objects.all()
		minerals = set()
		for mineral in minerallist:
			if not in_group(mineral.category):
				minerals.add(mineral)
		return render(request, 'minerals/index.html', {'minerals': minerals})