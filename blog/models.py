import datetime

from django.db import models


class Post(models.Model):
	title = models.CharField('Title', max_length=140)
	date = models.DateTimeField()	
	image = models.ImageField(upload_to='event_images/')
	text = models.CharField(max_length=300)

	def get_gummary(self):
		return self.text[:70]

	def __str__(self):
		return self.title