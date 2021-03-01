from django.db import models

# Create your models here.

class Student(models.Model):
	GENDER = (
		('F','Female'),
		('M','Male')
		)
	name = models.CharField(max_length = 256)
	roll_no = models.IntegerField()
	gender = models.CharField(max_length = 1, choices = GENDER)

	def __str__(self):
		return self.name

