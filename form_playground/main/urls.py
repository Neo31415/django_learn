
from django.urls import path
from main import views


urlpatterns = [
    path('', views.index),
    path('add_student', views.add_student, name = 'add_student'),
    path('students', views.students, name = 'students'),
]
