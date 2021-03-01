from django.shortcuts import render
from main import forms
from django.http import HttpResponseRedirect 

# Create your views here.

def index(request):
	context = {}
	response = render(request,'main/index.html',context)
	return response


def add_article(request):
	context = {'article_form' : forms.AddArticle }
	if request.method == "POST":
		articleform = forms.AddArticle(request.POST)
		if articleform.is_valid():
			article = articleform.save()
			context["success"] = True
	response = render(request,'main/add_article.html',context)
	return response