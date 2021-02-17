from django.http import Http404
from django.shortcuts import render, get_object_or_404
from main import models
# Create your views here.

def index(requests):
	# latest_articles = models.Article.objects.all()[:10]
	latest_articles = models.Article.objects.all().order_by('-created_at')[:10]
	context = {'latest_articles' : latest_articles}
	return render(requests,'main/index.html',context)

def article(requests,pk):
	# try:
	# 	article = models.Article.objects.get(id = pk)
	# except:
	# 	raise Http404()
	article = get_object_or_404(models.Article, id=pk)
	context = {'article' : article}
	return render(requests,'main/article.html',context)

def author(requests,pk):
	author = get_object_or_404(models.Author, id=pk)
	context = {'author' : author}
	return render(requests,'main/author.html',context)

def create_article(requests):
	authors = models.Author.objects.all()
	context={'authors' : authors}
	if requests.method == "POST":
		article_data = {
		"title" : requests.POST["title"],
		"content" : requests.POST["content"]
		}
		print("Content:"+requests.POST["content"])
		article = models.Article.objects.create(**article_data)
		author = models.Author.objects.get(pk = requests.POST["author"])
		article.authors.set([author])
		# author = models.Author.objects.filter(pk = requests.POST["author"])
		# article.authors.set(author)
		context["success"] = True
	
	response = render(requests,'main/create_article.html',context)
	return response