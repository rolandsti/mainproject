from django.db import models

# Create your models here.
class content(models.Model):
	title		= models.CharField(blank=False, max_length=100) #search for modal field reference
	description = models.TextField(blank=False, default='this is cool')
	morefields	= models.TextField(blank=False) #when adding new attriebut, you can use "default" property, that can be added