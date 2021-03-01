from django.shortcuts import render
from django.http import HttpResponseRedirect 
from main import forms
from main import models
# Create your views here.


def index(request):
	contex = {'form' : forms.ExampleForm}
	response = render(request,'index.html',contex)
	return response


def add_student(request):
	print(request.method)
	studentform = forms.StudentForm()
	if request.method == "POST":
		studentform = forms.StudentForm(request.POST)
		if studentform.is_valid():
			student = studentform.save()
			return HttpResponseRedirect('/students')

	contex = {'student_form' : studentform}
	response = render(request,'add_student.html',contex)
	return response


def students(request):
	students = models.Student.objects.all()
	contex = {'students' : students}
	response = render(request,'students.html',contex)
	return response