"""
verify that a sentence is made up of words.

e.g.

"isawe" -> i, is, a, saw, awe, we
"""


def is_sentence(inpt):
    for i in range(len(inpt)):
        if helper(inpt, i, i) == True:
            return True
    return False


def helper(inpt, head, tail):
    if tail == len(inpt) - 1:
        return True if is_word(inpt[head:tail + 1]) else False

    substr = inpt[head:tail + 1]

    if is_word(substr):
        return helper(inpt, tail + 1, tail + 1)
    else:
        return helper(inpt, head, tail + 1)


def is_word(word):
    words = ["i", "is", "a", "saw", "awe",
             "we", "like", "sam", "sung",
             "samsung", "ice", "cream", "and",
             "icecream", "man", "go", "mango"]
    return True if word in words else False

print is_sentence("isawe")  # T
print is_sentence("ilikesamsung")  # T
print is_sentence("iiiiiii")  # T
print is_sentence("ilikelikeimangoiii")  # T
print is_sentence("samsungandmango")  # T
print is_sentence("samsungandmangok")  # F
print is_sentence("isawep")  # F
