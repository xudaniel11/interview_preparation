"""
Merge two sorted linked lists in place.
"""
import unittest

def merge(headA, headB):
	A, B = headA, headB
	result = headA if headA.val < headB.val else headB

	while A != None and B != None:
		if A.val < B.val:
			nextA = A.next 
			while A.next != None and A.next.val <= B.val:
				A = A.next
				nextA = A.next
			A.next = B 
			A = nextA
		else:
			nextB = B.next
			while B.next.val != None and B.next.val < A.val:
				B = B.next
				nextB = B.next
			B.next = A 
			B = nextB
	return result

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

class TestMergeLL(unittest.TestCase):
	def test_usual_case(self):
		A = Node(0)
		A.next = Node(1)
		A.next.next = Node(1)
		A.next.next.next = Node(6)
	
		B = Node(0)
		B.next = Node(3)
		B.next.next = Node(5)
		B.next.next.next = Node(7)

		result = merge(A,B)
		self.assertEqual(result.val, B.val)
		self.assertEqual(result.next.next.val, 1)
		self.assertEqual(result.next.next.next.next.val, 3)

if __name__ == '__main__':
	unittest.main()

#should be 0, 0, 1, 1, 3, 5, 6, 7