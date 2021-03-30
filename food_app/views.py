from django.shortcuts import render
from py_edamam import Edamam
from .models import SavedBmiResults
import os

# FOOD_APP VIEWS

def home(request):
	return render(request, 'food_app/home.html')

def recipe_search(request):
	context = {}
	if request.method == "GET":
		edamam_conn = Edamam(recipes_appid=os.environ.get('WELLNESS_RECIPE_APPID'), recipes_appkey=os.environ.get('WELLNESS_RECIPE_APPKEY'))
		context['query'] = request.GET.get('searchRecipe')
		if context['query']:
			context['search_results'] = edamam_conn.search_recipe(context['query'])
	return render(request, 'food_app/recipe_search.html', context)

def food_search(request):
	context = {}
	if request.method == "GET":
		edamam_conn = Edamam(food_appid=os.environ.get('WELLNESS_FOOD_APPID'), food_appkey=os.environ.get('WELLNESS_FOOD_APPKEY'))
		context['query'] = request.GET.get('searchFood')
		if context['query']:
			context['search_results'] = edamam_conn.search_food(context['query'])
	return render(request, 'food_app/food_search.html', context)

def nutrient_search(request):
	context = {}
	if request.method == "GET":
		edamam_conn = Edamam(nutrition_appid=os.environ.get('WELLNESS_NUTRITION_APPID'), nutrition_appkey=os.environ.get('WELLNESS_NUTRITION_APPKEY'))
		context['query'] = request.GET.get('searchNutrient')
		if context['query']:
			context['query'] = context['query'].split('\r\n')
			context['search_results'] = edamam_conn.search_nutrient(context['query'])
	return render(request, 'food_app/nutrition_search.html', context)

def bmi_calculator(request):
	context = {}
	user = request.user
	if request.method == "GET":
		context['weight'] = request.GET.get('userWeight')
		context['height'] = request.GET.get('userHeight')
		
		if context['weight'] and context['height']:
			context['weight'] = int(context['weight'])
			context['height'] = int(context['height'])
			context['bmi_result'] = context['weight'] / (context['height']/100)**2
			print(context['bmi_result'])
	
	if request.method == "POST":
		print('hello')

	if user.savedbmiresults_set:
		context['queryset'] = user.savedbmiresults_set.all()
		print('queryset', context['queryset'])
	return render(request, 'food_app/bmicalculator.html', context)