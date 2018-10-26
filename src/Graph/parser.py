import xml.etree.ElementTree as ET
from xml.dom import minidom
from .models import Node, Group, Graph
import re

def remove_blank(file_with_blank):
	with open(file_with_blank, 'r') as f:
		lines = f.readlines()

	lines = [re.sub(r'[\n\t]*','',line) for line in lines]

	with open(file_with_blank, 'w') as f:
		f.writelines(lines)

def MyParcer(file, name):
	remove_blank(file)
	tree = ET.parse(file)
	data = tree.getroot()
	nodes = data.find('nodes')
	nodes_dict = {}

	for child in nodes:
		eid = child.attrib.get('eid')
		child_text = child.text
		nodes_dict[int(eid)] = (child_text)

	for node in nodes.findall('node'):
		nodes.remove(node)

	groups = data.find('groups')
	groups_dict = {}
	groups_text = {}

	for child in groups:
		x = sorted(tuple(child.attrib.get('groupped').split(' ')), reverse = True)
		for n in range(len(x)):
			x[n] = int(x[n])
		y = child.attrib.get('eid')
		groups_dict[int(y)] = (x)
		child_text = child.text
		groups_text[int(y)] = (child_text)

	groups_list = sorted(list(groups_dict), reverse = True)

	for group in groups.findall('group'):
		groups.remove(group)

	subgroups = []

	for i in groups_list:
		subgroups += groups_dict[i]

	def groupped_xml(l_group, n, text, id_in_db):
		u_group = ET.SubElement(l_group, "group", eid=str(n), id_in_db=id_in_db, text=text)
		for j in groups_dict[n]:
				if j in nodes_dict:
					obj = Node.objects.get_or_create(
						node_id=j, 
						parent_id=Group.objects.filter(graph=name).get(group_id=n), 
						graph=name,
						text=nodes_dict[j])
					id_db = str(Node.objects.filter(graph=name).get(node_id=j).id_in_db)
					node = ET.SubElement(
						u_group,
						"node", 
						eid=str(j), 
						id_in_db = str(id_db), 
						text=nodes_dict[j])
				else:
					obj = Group.objects.get_or_create(
						group_id=j, 
						parent_id=Group.objects.filter(graph=name).get(group_id=n), 
						graph=name, 
						text=groups_text[j])
					id_db = str(Group.objects.filter(graph=name).get(group_id=j).id_in_db)
					groupped_xml(u_group, j, groups_text[j], id_db)

	for k in groups_list:
		if k not in subgroups:
			obj = Group.objects.get_or_create(
				group_id=k, 
				parent_id=None, 
				graph=name, 
				text=groups_text[k])
			id_db = str(Group.objects.filter(graph=name).get(group_id=k).id_in_db)
			groupped_xml(groups, k, groups_text[k], id_db)

	only_nodes = set(subgroups) - set(groups_list)
	free_nodes = set(nodes_dict) - only_nodes

	for m in free_nodes:
		obj = Node.objects.get_or_create(
			node_id=m, 
			parent_id=None, 
			graph=name, 
			text=nodes_dict[m])
		id_db = str(Node.objects.filter(graph=name).get(node_id=m).id_in_db)
		node = ET.SubElement(
			nodes, 
			"node", 
			eid=str(m), 
			id_in_db = id_db, 
			text=nodes_dict[m])

	dom = minidom.parseString(ET.tostring(data, short_empty_elements=False)).toprettyxml(indent='\t')

	return dom




