from django.shortcuts import render
from py_edamam import Edamam

def home(request):
	return render(request, 'food_app/home.html')

def food_search(request):
	context = {}
	if request.method == "GET":
		edamam_conn = Edamam(recipes_appid='47e19430', recipes_appkey='3bb845ed77230a7e754635764ec810f6')
		context['query'] = request.GET.get('searchRecipe')
		if context['query']:
			context['search_results'] = edamam_conn.search_recipe(context['query'])
	return render(request, 'food_app/recipe_search.html', context)