"""
Given a directed graph, design an algorithm to find out whether there is a route 
between two nodes.

pg 54 of CTCI 
"""
import unittest
def search(start, end):
	q = [start]
	visited = set([])
	while len(q) > 0:
		curr = q.pop(0)
		if curr.val == end.val:
			return True
		elif curr not in visited:
			q.extend(curr.children)
			visited.add(curr)
	return False

class Digraph_node():
	def __init__(self, val):
		self.val = val
		self.children = []

class Test_If_Route(unittest.TestCase):
	def test_case_1(self):
		a = Digraph_node('A')
		b = Digraph_node('B')
		c = Digraph_node('C')
		d = Digraph_node('D')
		e = Digraph_node('E')
		a.children.append(b)
		b.children.extend([c, e])
		c.children.append(d)
		d.children.append(b)
		result = search(a, d)
		self.assertEqual(result, True)

	def test_case_2(self):
		a = Digraph_node('A')
		b = Digraph_node('B')
		c = Digraph_node('C')
		d = Digraph_node('D')
		a.children.append(b)
		b.children.append(c)
		d.children.append(a)
		result = search(a, d)
		self.assertEqual(result, False)

if __name__ == '__main__':
	unittest.main()



