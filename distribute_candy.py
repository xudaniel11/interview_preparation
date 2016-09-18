"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Sample Input :

Ratings : [1 2]
Sample Output : 3

The candidate with 1 rating gets 1 candy and candidate with rating cannot
get 1 candy as 1 is its neighbor. So rating 2 candidate gets 2 candies. 
In total, 2+1 = 3 candies need to be given out.
"""


def candies(arr):
    going_left = [1]
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            going_left.append(1)
        else:
            going_left.append(going_left[-1] + 1)

    going_right = [1]
    for i in reversed(range(len(arr) - 1)):
        if arr[i] > arr[i + 1]:
            going_right.append(going_right[-1] + 1)
        else:
            going_right.append(1)
    going_right.reverse()

    result = 0
    for i in range(len(arr)):
        result += max(going_left[i], going_right[i])
    return result

print candies([1, 4, 3, 3, 3, 1])
