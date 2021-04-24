import datetime

from django.db import models


class Post(models.Model):
	date = models.DateTimeField()
	title = models.CharField('Title', max_length=140)
	image = models.ImageField(upload_to='event_images/')
	text = models.CharField(max_length=300)
