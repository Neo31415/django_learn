from django import forms

class ExampleForm(forms.Form):
	names = forms.CharField(max_length = 100)
	about = forms.CharField(widget = forms.Textarea)
	active = forms.BooleanField()