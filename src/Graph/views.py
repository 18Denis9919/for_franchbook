from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Graph
from .forms import GraphCreateForm
from .parser import MyParcer

class GraphListView(ListView):
	queryset = Graph.objects.all()

class GraphDetailView(DetailView):
	queryset = Graph.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		path_file = self.object.file.path
		context['file'] = MyParcer(path_file, self.object)
		return context

class GraphCreateView(CreateView):
	template_name = 'form.html'
	form_class = GraphCreateForm

	def get_context_data(self, *args, **kwargs):
		context = super(GraphCreateView, self).get_context_data(*args, **kwargs)
		return context


