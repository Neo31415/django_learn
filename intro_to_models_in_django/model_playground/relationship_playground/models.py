from django.db import models

# Create your models here.

# many to one relationship
class Article(models.Model):
	title = models.CharField(max_length = 256)
	body = models.TextField()
	author = models.ForeignKey('Author', on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title

class Author(models.Model):
	name = models.CharField(max_length = 256)
	designation = models.CharField(max_length = 256)

	def __str__(self):
		return self.name


