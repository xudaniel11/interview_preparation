"""A function to find the longest continuous letter in a string."""


def longest_continuous_substr_letter(s):
    curr_letter = s[0]
    result = (1, curr_letter)
    num_curr = 1

    for i in range(1, len(s)):
        letter = s[i]
        if letter == curr_letter:
            num_curr += 1
            if num_curr > result[0]:
                result = (num_curr, curr_letter)
        else:
            curr_letter = letter
            num_curr = 1
    return result[1]

ex = "aabbbaa"
ex2 = "aabbb"
print longest_continuous_substr_letter(ex)  # b
print longest_continuous_substr_letter(ex2)  # b
