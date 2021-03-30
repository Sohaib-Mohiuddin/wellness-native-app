from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your USERS models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	age = models.IntegerField()
	height = models.IntegerField('Height(cm)')
	weight = models.IntegerField('Weight(kg)')
	
	def __str__(self):
		return f'{self.user.username} Profile'

	# def save(self):
	# 	super().save()

	# 	img = Image.open(self.image.path)
	# 	if img.height > 200 or img.width > 200:
	# 		new_size = (200, 200)
	# 		img.thumbnail(new_size)
	# 		img.save()
