from django.db import models

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length = 256)
	def __str__(self):
		return self.name

class Article(models.Model):
	title = models.CharField(max_length = 256)
	content = models.TextField(max_length = 256)
	created_at = models.DateTimeField(auto_now_add = True)
	# In this author is not a list...it is a relationship manager
	# use ```author.all()```
	authors = models.ManyToManyField('Author')
	
	def __str__(self):
		return self.title