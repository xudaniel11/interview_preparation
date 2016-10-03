# Problem statement:
# Given a sentence and the maximum number of characters each line can
# hold, we will stretch each line so that the text starts and ends at each
# margin.

# Input:
# One paragraph (without "\n" in the input)
# Max number of characters that the line can hold

# Output:
# Print the text justified sentence to the screen

# Rules:
# Left justify if the line contains a single word (Flush left)
# Fully justify if the line has multiple words
# fully justified means there can't be a space following the last word
# in a line. the first and last chars of a line must be letters belonging
# to a word

# Words as evenly spaced as possible (2 - 3 - 3 - 3 is better than
# 2 - 2 - 2 - 5) numbers mean the number of spaces in between each word
# You can assume no word is > the length of the line.
# Print as few lines as possible

# Example:
# Ruby is a dynamic, open source programming language with a focus on
# simplicity and productivity. It has an elegant syntax that is natural to
# read and easy to write.
"""
max line length is 50:
Ruby  is  a  dynamic,  open   source   programming
language  with   a   focus   on   simplicity   and
productivity. It has an  elegant  syntax  that  is
natural   to   read    and    easy    to    write.
"""

# left justify when the word takes up the entire line
# left justify when the word doesnt take up the entire line but
# is the last line <--

# Ruby  is  a  dynamic,  open

# 1) grab first N characters
# 2) cutting off the last word if its not a whole word
# 3) adding spaces in between each word
# 4) checking if the string i have so far is fully justified

# by adding spaces in between each word, i have to cut the last word out again


def main(paragraph, n):
    result = []

    def justify(paragraph, n):

        first_n_words = []
        paragraph_word = paragraph.split(' ')  # ['a','b','c']
        num_words = len(paragraph_word)
        word_counter = 0
        line = ' '.join(first_n_words)
        while len(line) < 50:
            if word_counter >= num_words:
                break

            first_n_words.append(paragraph_word[word_counter])
            word_counter += 1
            line = ' '.join(first_n_words)
            if len(line) >= 50:
                first_n_words.pop()
                line = ' '.join(first_n_words)
                word_counter -= 1
                break

        num_chars_leftover = n - len(line)
        line_spaces = []
        for word in line.split():
            line_spaces.append(word)
            if num_chars_leftover > 0:
                line_spaces.append(' ')
                num_chars_leftover -= 1
            else:
                break

        added_spaces = ' '.join(line_spaces)
        result.append(added_spaces)
        rest_of_words = " ".join(paragraph.split()[word_counter:])
        if word_counter < num_words:
            justify(rest_of_words, n)
        else:
            return

    justify(paragraph, n)
    return result

import unittest


class TestJustify(unittest.TestCase):

    def test_1(self):
        p = "Ruby is a dynamic, open source programming language with a focus on simplicity and productivity. It has an elegant syntax that is natural to read and easy to write."
        n = 50
        print main(p, n)

if __name__ == "__main__":
    unittest.main()


# ['a','b','c'] --> 'abc' 'a b c'
#('abc','basdf','c1') =  'abcbasdfc1'
