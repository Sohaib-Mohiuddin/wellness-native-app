from django.db import models
from django.contrib.auth.models import User

# Create your Calculator models here.

class SavedBmiResults(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	weight = models.IntegerField(default=0, verbose_name='weight')
	height = models.IntegerField(default=0, verbose_name='height')
	bmi_result = models.FloatField(default=0, verbose_name="bmiresult", blank=True)

	def __str__(self):
		return f'{self.user.username} BMI Result(s)'

class SavedBmrResults(models.Model):
	user_bmr = models.ForeignKey(User, on_delete=models.CASCADE)
	weight = models.IntegerField(default=0, verbose_name='weight')
	height = models.IntegerField(default=0, verbose_name='height')
	age = models.IntegerField(default=0, verbose_name='age')
	sex = models.CharField(default='-', verbose_name='sex', max_length=50)
	bmr_result = models.FloatField(default=0, verbose_name="bmrresult", blank=True)

	def __str__(self):
		return f'{self.user_bmr.username} BMR Result(s)'