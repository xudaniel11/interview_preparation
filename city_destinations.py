"""
Given an input city, return the cities that can be reached.

Algorithm: iterate through the initial list in order to create the adjacency matrix. 
Then, use DFS to figure out what cities can be connected to from the input one.
"""
import unittest

def city_destinations(cities, original_city):

	# build adjacency list
	ad_list = adjacencyList()
	for i, (source, destination) in enumerate(cities):
		if ad_list.has_city(source):
			ad_list.add_destination(source, destination)
		elif not ad_list.has_city(source):
			ad_list.add_source(source)
			ad_list.add_destination(source, destination)
	
	# DFS
	visited = set()
	stack = []
	stack.append(original_city)
	stack.extend(ad_list.get_destinations(original_city))
	while stack:
		city = stack.pop()
		print city
		if city not in visited:
			visited.add(city)
			destinations = ad_list.get_destinations(city)
			if destinations:
				stack.extend(destinations)
	return visited

class adjacencyList():
	def __init__(self):
		self.ad_list = {}

	def add_source(self, city):
		self.ad_list[city] = []

	def add_destination(self, source, destination):
		self.ad_list[source].append(destination)

	def has_city(self, city):
		return self.ad_list.has_key(city)

	def get_destinations(self, source):
		return self.ad_list.get(source)


class TestCityDestinations(unittest.TestCase):
	"""
	SFO : [NYC, SAC, LAX, DC]
	NYC : [SFO, OAK]
	SAC : [LAX]
	DEL : [AUX]
	"""
	def test_usual_case(self): 
		ex = [("SFO","NYC"),("NYC", "SFO"), ("NYC", "OAK"), ("SFO", "SAC"), ("SAC", "LAX"), ("SFO", "LAX"), ("DEL", "AUX"), ("SFO", "DC")] 
		result = city_destinations(ex, "SFO")
		self.assertItemsEqual(result, ["NYC", "SAC", "LAX", "DC", "SFO", "OAK"])

	def test_cycle(self):
		ex = [("SFO", "NYC"), ("NYC", "SFO")]
		result = city_destinations(ex, "SFO")
		self.assertItemsEqual(result, ["SFO", "NYC"])

	def test_no_destinations(self):
		ex = [("SFO", "NYC"), ("DEL", "LAX")]
		result = city_destinations(ex, "SFO")
		self.assertItemsEqual(result, ["SFO", "NYC"])

if __name__ == '__main__':
	unittest.main()

