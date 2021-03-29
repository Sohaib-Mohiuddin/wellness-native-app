from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm

# USERS VIEWS

def register(request):
	context = {}

	if request.method == 'POST':
		context['form'] = UserRegistrationForm(request.POST)
		if context['form'].is_valid():
			context['form'].save()
			username = context['form'].cleaned_data.get('username')
			messages.success(request, f'Successfully Registered As { username }')
			return redirect('login')
	else:
		context['form'] = UserRegistrationForm()
	return render(request, 'users/register.html', context)