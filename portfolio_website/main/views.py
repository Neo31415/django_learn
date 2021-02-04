from django.shortcuts import render

def index(requests):
	context = {}
	response = render(requests,'main/index.html')
	return response 

# Create your views here.
