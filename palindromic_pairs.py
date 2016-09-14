import unittest


def is_palindrome(s):
    if s is None:
        return False

    limit = len(s) / 2
    for i in range(limit):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def palindrome_pairs(ls):
    dt = {}
    for i, word in enumerate(ls):
        dt[word[::-1]] = word

    result = []
    for index, word in enumerate(ls):
        substrings = substrings_from_word(word, dt)
        for substr in substrings:
            substr = substr[::-1]
            if not substr in ls:
                continue
            left_concat = substr + word
            right_concat = word + substr
            if is_palindrome(left_concat):
                result.append([substr, word])
            elif is_palindrome(right_concat):
                result.append([word, substr])
    return result


def substrings_from_word(word, dt):
    words = []
    for i in range(len(word)):
        temp = word[i:]
        if temp in dt:
            words.append(temp)
    return words

print palindrome_pairs(["mat", "tam", "bat"])
print palindrome_pairs(["bag", "gab", "ab", "bbbbag"])
print palindrome_pairs(["mms", "sssmm"])


"""
ls = 'ga', 'bag'
pass 1: dt = {ag:ga, gab:bag} reversed the k,v

, bag}
'ga'
for key in dt.keys():
    if word_im_pairing == key[1:]
        result.append([word_im_pairing, key])
pass2: ga? ag, bag

ga, bbbbag #odd no. letters case when the two words are of diff length

ga, ag #even no. letters

gabag 

ls = ["gab", "bag", "bbbbag", "ba"]
dt = {gab: bag, bag: gab, bbbbag: gabbbb, ba: ab}
"gab" bag, {"ba" "gab"} gab, ab, b?
"bbbbag" "bbbag", "bbag", "bag", "ag, "g"? k number of checks where k is the initial word 

2nd phase: the current word im looking at. check to see if 
every one of its substrings are in the dict? 

"bag" 

Test 1: naive case on line 8
Test 2: initial list is empty
Test 3: initial list is None
Test 4: ["ga", "bag"] 

["ga", "hi", "bag"]
dict = { ga: ag, hi: ih, bag: gab:,  
ag: ga , a:g, i: i} 

"ga"
"bag" 

"ga" 
"ag", "_ag",

"bag"
"ag" , "ga"

"a"+suffix
"b"+suffix

"yay" --> "yay"
"ay" --> "ya"

"ga", "bag"

"bag" --> "gab"
"ag" --> "ga" 

"a" --> "a"

"ga", "bag" 

"bag" --> 'bag', 'ag' 

'ag' is in dt
'bag' is in dt 

word[1:] 
"""


# class TestIsPalindrome(unittest.TestCase):

#     def test_1(self):
#         example = "kayak"
#         expect = True
#         result = is_palindrome(example)
#         self.assertEqual(result, expect)

#     def test_2(self):
#         example = ""
#         expect = True
#         result = is_palindrome(example)
#         self.assertEqual(result, expect)

#     def test_3(self):
#         example = None
#         expect = False
#         result = is_palindrome(example)
#         self.assertEqual(result, expect)

#     def test_4(self):
#         example = "hello world"
#         expect = False
#         result = is_palindrome(example)
#         self.assertEqual(result, expect)

# if __name__ == "__main__":
#     unittest.main()
