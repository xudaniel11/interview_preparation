"""
Given a set of distinct integers, S, return all possible subsets.

 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
Also, the subsets should be sorted in ascending ( lexicographic ) order.
The list is not necessarily sorted.
Example :

If S = [1,2,3], a solution is:

[
  [],
  [1],
  [1, 2],
  [1, 2, 3],
  [1, 3],
  [2],
  [2, 3],
  [3],
]
"""


def subsets_wrong(arr):
    result = [[]]
    for i, num in enumerate(arr):
        new_results = []
        for j, subset in enumerate(result):
            # wrong bc im assigning a reference to the original object,
            # not copying it
            tmp = subset
            tmp.append(num)
            new_results.append(tmp)
        result.extend(new_results)
    return result


def subsets(arr):
    result = [[]]
    for i, num in enumerate(arr):
        new_results = []
        for j, subset in enumerate(result):
            new_results.append(subset + [num])
        result.extend(new_results)
    return result

print subsets([1, 2, 3])
