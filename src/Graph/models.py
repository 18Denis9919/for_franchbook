import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from .utils import *

def upload_location(instance, filename):
	return "%s/%s" %(instance.name, filename)

class Graph(models.Model):
	name 		= models.CharField(max_length=30)
	file 		= models.FileField(upload_to=upload_location)
	timestamp	= models.DateTimeField(auto_now_add = True)
	slug		= models.SlugField(null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('graph:detail', kwargs = {'slug': self.slug}) 
	
	class Meta:
		ordering = ['-timestamp', ]

class Node(models.Model):
	id_in_db	= models.AutoField(primary_key=True)
	node_id 	= models.IntegerField()
	parent_id 	= models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
	graph 		= models.ForeignKey('Graph', on_delete=models.CASCADE)
	text 		= models.CharField(max_length=30)

	
class Group(models.Model):
	id_in_db	= models.AutoField(primary_key=True)
	group_id	= models.IntegerField()
	parent_id 	= models.ForeignKey('self', on_delete=models.CASCADE, null=True)
	graph 		= models.ForeignKey('Graph', on_delete=models.CASCADE)
	text		= models.CharField(max_length=30)
	
		
def tl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	

pre_save.connect(tl_pre_save_receiver, sender=Graph)
