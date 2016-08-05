"""
Given a mapping of alphabets to integers as follows: 

1 = A 
2 = B 
3 = C 
... 
26 = Z 

Given any combination of the mapping numbers as string, return the number of ways in which the input string can be split into sub-strings and represented as character strings. For e.g. given 
"111" -> "AAA", "AK", "KA" -> 3 
Valid combinations are ({1,1,1}, {1,11},{11,1}) = 3 
"11" -> "AA", "K" -> 2 
Valid combinations are ({1,1},{11}) = 2 
"123" -> "ABC", "LC", "AW" -> 3 
Valid combinations are ({1,2,3},{1,23},{12,3}) = 3 

You don't have to return all the mappings, only the number of valid mappings.

Follow up harder question: return all the mappings LOL
"""
import unittest

def number_letter_combinations(input_str):
	cache = [1, 1]
	for i in range(1, len(input_str)):
		if int(input_str[i-1] + input_str[i]) < 27:
			cache.append(int(cache[i]) + int(cache[i-1]))
		else:
			cache.append(int(cache[i]))
	return cache[-1]

class TestNumberLetterCombinations(unittest.TestCase):
	def test_case_1(self):
		input_str = "123"
		result = number_letter_combinations(input_str)
		self.assertEqual(result, 3)

	def test_case_2(self):
		input_str = "1212"
		result = number_letter_combinations(input_str)
		self.assertEqual(result, 5)

	def test_case_3(self):
		input_str = "1324"
		result = number_letter_combinations(input_str)
		self.assertEqual(result, 4)

if __name__ == '__main__':
	unittest.main()

