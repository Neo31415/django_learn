from django.shortcuts import render
from main import forms
# Create your views here.


def index(request):
	contex = {'form' : forms.ExampleForm}
	print(forms.ExampleForm.as_table)
	response = render(request,'index.html',contex)
	return response