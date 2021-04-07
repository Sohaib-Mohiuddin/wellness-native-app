from django.shortcuts import render, redirect
from django.contrib import messages
from py_edamam import Edamam
from .models import SavedBmiResults, SavedBmrResults
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
				context = {
					'query': query,
					'search_results': search_results
				}
				messages.success(request, f'Returned Nutrition Facts!')
			except: 
				messages.warning(request, f'Cannot Find Nutritional Values. Check Format/Spelling Of Ingredients List!')
				# messages.warning(request, f'Refreshed!')
				# return redirect('nutrient-search')
		
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

	if user.is_authenticated:
		if user.savedbmiresults_set:
			context['queryset'] = user.savedbmiresults_set.all()
			print('queryset', context['queryset'])

	if request.method == "POST":
		weight = request.POST.get('readonlyweight')
		height = request.POST.get('readonlyheight')
		bmiResult = request.POST.get('bmiResult')

		print(weight, height, bmiResult)

		if weight and height and bmiResult:
			save_result = SavedBmiResults(user=user, weight=weight, height=height, bmi_result=bmiResult)
			save_result.save()
			messages.success(request, f'Saved Your Weight, Height, And BMI Result!')
		else:
			messages.warning(request, f'Could Not Save. Try Again!')

	return render(request, 'food_app/bmicalculator.html', context)

def bmr_calculator(request):
	'''
	For men: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) + 5

	For women: BMR = 10 x weight (kg) + 6.25 x height (cm) – 5 x age (years) – 161
	'''
	context = {}
	user = request.user
	if request.method == "GET":
		context['weight'] = request.GET.get('userWeight')
		context['height'] = request.GET.get('userHeight')
		context['age'] = request.GET.get('userAge')
		context['sex'] = request.GET.get('bmrsex')

		if context['weight'] and context['height'] and context['age'] and context['sex']:
			context['weight'] = int(context['weight'])
			context['height'] = int(context['height'])
			context['age'] = int(context['age'])

			if context['sex'] == 'Male':
				context['bmr_result'] = 10 * context['weight'] + 6.25 * context['height'] - 5 * context['age'] + 5
				print(context['bmr_result'])
			else:
				context['bmr_result'] = 10 * context['weight'] + 6.25 * context['height'] - 5 * context['age'] - 161
				print(context['bmr_result'])

	if user.is_authenticated:
		if user.savedbmrresults_set:
			context['queryset'] = user.savedbmrresults_set.all()
			print('queryset', context['queryset'])

	if request.method == "POST":
		weight = request.POST.get('readonlyweight')
		height = request.POST.get('readonlyheight')
		age = request.POST.get('readonlyage')
		sex = request.POST.get('readonlysex')
		bmrResult = request.POST.get('bmrResult')

		print(weight, height, age, sex, bmrResult)

		if weight and height and age and sex and bmrResult:
			save_result = SavedBmrResults(user_bmr=user, weight=weight, height=height, age=age, sex=sex, bmr_result=bmrResult)
			save_result.save()
			messages.success(request, f'Saved Your Weight, Height, And BMI Result!')
			return redirect('bmr-calculator')
		else:
			messages.warning(request, f'Could Not Save. Try Again!')

	return render(request, 'food_app/bmrcalculator.html', context)

def measurement_converter(request):
	return render(request, 'food_app/measurementconverter.html')

def other_calculators(request):
	return render(request, 'food_app/othercalculators.html')

def tea_calculator(request):
	return render(request, 'food_app/teacalculator.html')

