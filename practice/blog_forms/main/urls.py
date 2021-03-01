
from django.urls import path,include
from main import views

urlpatterns = [
    path('', views.index),
    path('add_article', views.add_article, name = 'add_article'),
]
