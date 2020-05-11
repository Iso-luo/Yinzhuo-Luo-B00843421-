"""
Task 9
Write a function called ‘most_frequent’ that 
takes a string and prints the letters in decreasing order of frequency.
"""


def most_frequent(s):
    l = []
    [l.append(i) for i in s]
    l.sort()
    return "".join(l)

print(most_frequent("zhksnfvks"))

