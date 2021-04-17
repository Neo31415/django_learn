# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Article
from .forms import ArticleModelForm
from django.urls import reverse

# Create your views here.

def index(request):
	context = {}
	response = render(request,'blog/index.html',context)
	return response

class ArticleCreateView(CreateView):
	template_name = 'blog/article_create.html' #overriding default template
	form_class = ArticleModelForm
	# queryset = Article.objects.all()
	success_url = "/blog"

class ArticleUpdateView(UpdateView):
	template_name = 'blog/article_create.html' #overriding default template
	form_class = ArticleModelForm
	# success_url = "/blog"
	def get_object(self):
		id_ = self.kwargs.get("id")
		print(id_)
		return get_object_or_404(Article,id=id_)


class ArticleListView(ListView):
	# Gives "object_list" to the template
	# by default expects <APP_NAME>/<MODEL_NAME>_list.html as  template
	template_name = 'blog/article_list.html' #overriding default template
	queryset = Article.objects.all()


class ArticleDetailView(DetailView):
	# Gives "object" to the template
	template_name = 'blog/article_detail.html'
	# queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		print(id_)
		return get_object_or_404(Article,id=id_)


class ArticleDeleteView(DeleteView):
	# Gives "object" to the template
	template_name = 'blog/article_delete.html'
	# queryset = Article.objects.all()
	# success_url = "/blog"


	def get_object(self):
		id_ = self.kwargs.get("id")
		print(id_)
		return get_object_or_404(Article,id=id_)

	def get_success_url(self):
		return reverse("article-list")
