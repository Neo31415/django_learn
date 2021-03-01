from django import forms
from main import models

class AddArticle(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = '__all__'