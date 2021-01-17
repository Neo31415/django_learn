from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	developed_by = "Sumit Aggarwal"
	mentors = ["Pramod","Rajni","Umesh","Sumit","Mohit"]
	context = {
	"developer" : developed_by,
	"mentors" : mentors
	}
	# response = HttpResponse("Hello World")
	response = render(request,"index.html",context)
	return response