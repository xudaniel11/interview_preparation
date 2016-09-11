"""
Given a string of integers, and an integer 'remove', return the min number the 
string can be after removing 'remove' number of integer strings.
"""


def calculate_min(coordinates, remove):
    if remove == 0:
        return coordinates

    nums = []
    for i, num in enumerate(coordinates):
        tmp = coordinates[:i] + coordinates[i + 1:]
        nums.append(tmp)
    new_coordinates = min(nums)
    return calculate_min(new_coordinates, remove - 1)

print calculate_min("2615437", 3)
