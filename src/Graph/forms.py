from django import forms
from .models import Graph

class GraphCreateForm(forms.ModelForm):
	class Meta:
		model = Graph
		fields = [
		'name',
		'file'
		]
		labels = {
			'name':'Название',
			'file':'Файл'
		}