from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from food_app.models import SavedBmiResults

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	age = forms.IntegerField()
	height = forms.IntegerField(label='Height(cm)')
	weight = forms.IntegerField(label='Weight(kg)')
	class Meta:
		model = User
		fields = ['username', 'email',, 'age', 'weight', 'height' 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
    	model = User
    	fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image', 'age', 'weight', 'height']

