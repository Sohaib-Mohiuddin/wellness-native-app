from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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

@login_required
def profile(request):
	context = {}
	if request.method == 'POST':
		context['user_form'] = UserUpdateForm(request.POST, instance=request.user)
		context['profile_form'] = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if context['user_form'].is_valid() and context['profile_form'].is_valid():
			context['user_form'].save()
			context['profile_form'].save()
			messages.success(request, f'Profile Has Been Updated')
			return redirect('profile')
	else:
		context['user_form'] = UserUpdateForm(instance=request.user)
		context['profile_form'] = ProfileUpdateForm(instance=request.user.profile)


	return render(request, 'users/profile.html', context)