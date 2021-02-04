from django.db import models

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
	email = models.EmailField(null = True)
	gender = models.CharField(max_length = 1, choices = GENDER, null = True)

def _str_(self):
	return self.name