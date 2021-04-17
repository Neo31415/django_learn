from django import forms
from blog import models

class ArticleModelForm(forms.ModelForm):
	class Meta:
		model = models.Article 
		fields = '__all__'