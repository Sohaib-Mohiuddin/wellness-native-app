from django import forms
from django.contrib.auth.models import User
from food_app.models import SavedBmiResults

class UserBmiResultForm(forms.ModelForm):
    weight = forms.IntegerField()
    height = forms.IntegerField()
    class Meta:
    	model = SavedBmiResults
    	fields = ['weight', 'height']