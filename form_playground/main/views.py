from django.shortcuts import render

# Create your views here.


def index(request):
	contex = {}
	response = render(request,'index.html',contex)
	return response