"""wellness_native_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views
from food_app import views as food_app_views
from users import views as users_views

urlpatterns = [
    # admin view
    path('admin/', admin.site.urls),

    # login logout views
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', users_views.register, name='register'),

    # food_app views
    path('', food_app_views.home, name='food-app-home'),
    path('recipe-search/', food_app_views.recipe_search, name='recipe-search'),
    path('food-search/', food_app_views.food_search, name='food-search'),
    path('nutrient-search/', food_app_views.nutrient_search, name='nutrient-search')
]
