from django.urls import re_path
from .views import GraphListView, GraphDetailView, GraphCreateView

app_name = 'graph'

urlpatterns = [
    re_path(r'^$', GraphListView.as_view(), name='list'),
    re_path(r'^create/$', GraphCreateView.as_view(), name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', GraphDetailView.as_view(), name='detail')
    
]