"""
Author: Jasmine Lee
jasminelee988@gmail.com 

To run:
$ python boggle_solver.py 

Description: boggle solver using DFS
"""


def main(arr):  # return a list of strings
    def find_words(curr_word, curr_index, indices_path):  # returns a list of words
        print curr_word, curr_index, indices_path
        i, j = curr_index
        indices_path.add(curr_index)
        adjacents = get_adjacent_indices(arr, i, j, indices_path)
        for coordinate in adjacents:
            x, y = coordinate
            indices_path.add(coordinate)
            letter = arr[x][y]
            curr_word += letter
            if is_word(curr_word) and adjacents:  # add word indices to used_letters
                used_indices.extend(indices_path)
                result.append(curr_word)
                # return
            elif is_word(curr_word) and not adjacents:
                used_indices.extend(indices_path)
                result.append(curr_word)
                return
            elif not is_word(curr_word) and adjacents:
                find_words(curr_word, (x, y), indices_path)
            elif not is_word(curr_word) and not adjacents:
                continue

    def get_adjacent_indices(arr, i, j, indices_path):
        n, m = len(arr), len(arr[0])
        valid_indices = []
        top_row = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)]
        for top in top_row:
            x, y = top
            if x >= 0 and 0 <= y < m and not top in used_indices:
                valid_indices.append(top)

        if j > 0 and not (i, j - 1) in used_indices:  # left
            valid_indices.append((i, j - 1))

        if j < m - 1 and not (i, j + 1) in used_indices:  # right
            valid_indices.append((i, j + 1))

        bottom_row = [(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        for bottom in bottom_row:
            x, y = bottom
            if 0 <= x < n and m > y >= 0 and not bottom in used_indices:
                valid_indices.append(bottom)

        valid_indices = remove_dupes(valid_indices, indices_path)
        return valid_indices

    used_letters = []  # a list of indices of used letters
    # n is the number of rows, m is the num of cols
    n, m = len(arr), len(arr[0])
    result = []
    used_indices = []
    for i in range(n):
        for j in range(m):
            curr_letter = arr[i][j]
            find_words(curr_letter, (i, j), set([(i, j)]))
    return result


def remove_dupes(proposed_ls, path_set):
    ls = []
    for proposed in proposed_ls:
        if proposed not in path_set:
            ls.append(proposed)
    return ls


def is_word(word):
    # 'asy' and 'fall' are red herrings
    words = ['rat', 'sun', 'asy', 'fib', 'on', 'all']
    for w in words:
        if sorted(w) == sorted(word):
            return True
    return False

import unittest


class TestBoggleSolver(unittest.TestCase):

    def test_1(self):
        """
        RAT
        XSU
        IYN
        """
        ex = [['r', 'a', 't'], ['x', 's', 'u'], ['i', 'y', 'n']]
        expected = ['rat', 'sun'].sort()
        result = main(ex).sort()
        self.assertEqual(result, expected)

    def test_2(self):
        # doesn't work bc of backtracking bug
        """
        S M E F
        R A T D
        L O N I
        K A F B
        """
        ex = [['s', 'm', 'e', 'f'], ['r', 'a', 't', 'd'],
              ['l', 'o', 'n', 'i'], ['l', 'a', 'f', 'b']]
        expected = ['rat', 'fib', 'on', 'all']
        result = main(ex)
        print result

if __name__ == "__main__":
    unittest.main()

"""
NOTES FROM COLLABEDIT

Example of what a boggle grid looks like:
S M E F
R A T D
L O N I
K A F B

Potential answers:
RAT

M
A T

R
 O
  F

given is_valid(word), which takes in a str and returns a boolean

3 x 3
S M E
R A T
L O N

curr_letter = R
adjacent_letters = A, O, L, S, M
R A
  ^
curr_letter = A
adjacent_letters =  T, N, O, L, R, S, M, E
R A T # check whether it is a valid word. record its indices, add word to my list of words result
    ^
curr_letter = T
adjacent_letters = N, O, A, M, E
                         ^
R A T O
adjacent_letters for O if there are unused adjacent letters.
# stop when there are no more unused adjacent letters and curr word is not
# valid.

"""
