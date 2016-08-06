"""
Given a matrix of 1's and 0's, transform it into a resulting matrix where a number in a cell indicates how close the nearest 1 was in the original matrix.

Daniel's solution calculates the manhattan distance (moves orthogonally), whereas my solution calculates distance using any arbitrary movement, e.g. 
a number 1 directly in the upper right corner of a cell would be only 1 away from that cell.

E.g.:
[[0,0,1,0,0],
 [1,1,1,0,1],
 [1,0,1,0,0],
 [0,0,0,0,1],
 [1,0,0,0,0]])

should become:
[[1,1,0,1,1], 
 [0,0,0,1,0],
 [0,1,0,1,1],
 [1,1,1,1,0],
 [0,1,2,1,1]])
"""
import numpy as np
import unittest

def binary_matrix(mat):
	m, n = mat.shape
	result = np.zeros((m,n))
	for i0 in range(m): #col
		for j0 in range(n): #row
			if mat[i0, j0] == 1:
				continue
			else:
				coordinate_closest_one = find_distance(mat, i0, j0)
				if coordinate_closest_one != None:
					i1, j1 = coordinate_closest_one
					distance = max(abs(i0-i1), abs(j0-j1))
					result[i0,j0] = distance 

	return result

def find_distance(mat, i, j):
	q = [(i,j)]
	visited = set((i,j)) 
	#BFS
	while len(q) > 0:
		curr_i, curr_j = q.pop(0)
		if mat[curr_i, curr_j] == 1:
			return (curr_i,curr_j)
		else:
			children = children_of(mat, curr_i, curr_j)
			for child in children:
				if child not in visited:
					q.extend(children)
					visited.update(children)
	return None

def children_of(mat, i, j):
	m, n = mat.shape
	left_top_corner = (i-1, j-1)
	top = (i-1, j)
	right_top_corner = (i-1, j+1)
	left = (i, j-1)
	right = (i, j+1)
	left_bottom_corner = (i+1, j-1)
	bottom = (i+1, j)
	right_bottom_corner = (i+1, j+1)

	potential_children = [left_top_corner, top, right_top_corner, left, right, left_bottom_corner, bottom, right_bottom_corner]
	# print len(children), children
	children = []
	for index, (k,l) in enumerate(potential_children):
		if k < 0 or l < 0 or k >= m or l >= n: # if out of boundaries
			continue
		else:
			children.append((k,l))
	return children

class TestBinaryMatrix(unittest.TestCase):
	def test_case_1(self):
		testMatrix_1 = np.matrix([[0,0,1,0,0],[1,1,1,0,1],[1,0,1,0,0],[0,0,0,0,1],[1,0,0,0,0]])
		answer = np.matrix([[1,1,0,1,1], [0,0,0,1,0],[0,1,0,1,1],[1,1,1,1,0],[0,1,2,1,1]])
		result = binary_matrix(testMatrix_1)
		print "Test 1: answer followed by result"
		print answer
		print result

	def test_case_2(self):
		testMatrix_2 = np.matrix([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])
		answer = np.zeros((5,5))
		result = binary_matrix(testMatrix_2)
		print "Test 2: answer followed by result"
		print answer
		print result

	def test_case_3(self):
		testMatrix_3 = np.matrix([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
		answer = np.zeros((5,5))
		result = binary_matrix(testMatrix_3)
		print "Test 3: answer followed by result"
		print answer
		print result

	def test_case_4(self):
		testMatrix_4 = np.matrix([[1,1,1,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,1,1,1,1]])
		answer = np.matrix([[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2],[1,1,1,1,1],[0,0,0,0,0]])
		result = binary_matrix(testMatrix_4)
		print "Test 4: answer followed by result"
		print answer
		print result

if __name__ == '__main__':
	unittest.main()