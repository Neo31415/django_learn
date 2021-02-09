from django.db import models
from django.core.validators import (
EmailValidator,
MaxValueValidator,
MinValueValidator,
URLValidator,
validate_slug
	)

from main.validators import (
validate_even_number
	)

# Create your models here.

class Student(models.Model):
	GENDER = (
		('f',"Female"),
		('m',"Male"),
		('u',"Undesclosed")
		)
	name = models.CharField(max_length=100)
	roll_number = models.IntegerField(unique = True)
	address = models.TextField(null = True)
	phone_number = models.CharField(max_length = 15, null = True, blank = True)
	email = models.CharField(max_length = 100, null = True, validators=[EmailValidator("Invalid Email Adderss")])
	gender = models.CharField(max_length = 1, choices = GENDER, null = True)
	age = models.IntegerField(null=True, validators=[MaxValueValidator(150),MinValueValidator(25),validate_even_number])
	slug = models.CharField(max_length = 100, null=True, validators=[validate_slug])

	def __str__(self):
		return self.name