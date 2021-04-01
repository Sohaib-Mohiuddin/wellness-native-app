from django.shortcuts import render, redirect
from django.contrib import messages
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
		query = request.GET.get('searchRecipe')
		if query:
			try:
				search_results = edamam_conn.search_recipe(query)
				messages.success(request, f'Returned { query }(s)!')
				context = {
					'query': query,
					'search_results': search_results
				}
			except:
				messages.warning(request, f'Cannot Find { query }. Check Format/Spelling Of Recipe!')
				# messages.warning(request, f'Refreshed Page!')
				# return redirect('recipe-search')
	
	return render(request, 'food_app/recipe_search.html', context)

def food_search(request):
	context = {}
	if request.method == "GET":
		edamam_conn = Edamam(food_appid=os.environ.get('WELLNESS_FOOD_APPID'), food_appkey=os.environ.get('WELLNESS_FOOD_APPKEY'))
		query = request.GET.get('searchFood')
		if query:
			try:
				search_results = edamam_conn.search_food(query)
				messages.success(request, f'Returned { query }(s)!')
				context = {
					'query': query,
					'search_results': search_results
				}
			except:
				messages.warning(request, f'Cannot Find { query }. Check Format/Spelling Of Food Search!')
				# messages.warning(request, f'Refreshed Page!')
				# return redirect('recipe-search')
	
	return render(request, 'food_app/food_search.html', context)

def nutrient_search(request):
	context = {}
	if request.method == "GET":
		edamam_conn = Edamam(nutrition_appid=os.environ.get('WELLNESS_NUTRITION_APPID'), nutrition_appkey=os.environ.get('WELLNESS_NUTRITION_APPKEY'))
		query = request.GET.get('searchNutrient')
		if query:
			query = query.split('\r\n')
			try: 
				search_results = edamam_conn.search_nutrient(query)
				messages.success(request, f'Returned Nutrition Facts!')
				context = {
					'query': query,
					'search_results': search_results
				}
			except: 
				messages.warning(request, f'Cannot Find Nutritional Values. Check Format/Spelling Of Ingredients List!')
				# messages.warning(request, f'Refreshed!')
				# return redirect('nutrient-search')
		
	return render(request, 'food_app/nutrition_search.html', context)

def bmi_calculator(request):
	user = request.user
	if request.method == "GET":
		weight = request.GET.get('userWeight')
		height = request.GET.get('userHeight')
		
		if weight and height:
			weight = int(weight)
			height = int(height)
			bmi_result = weight / (height/100)**2
			print(bmi_result)
	
	if request.method == "POST":
		print('hello')

	if user.savedbmiresults_set:
		queryset = user.savedbmiresults_set.all()
		print('queryset', queryset)

	context = {
		'weight': weight,
		'height': height,
		'bmi_result': bmi_result,
		'queryset': queryset,
	}
	return render(request, 'food_app/bmicalculator.html', context)