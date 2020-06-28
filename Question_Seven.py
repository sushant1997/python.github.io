"""
7.Write a Python function that takes a list of words and returns the length of the
longest one.
"""

def listCounter(str):
    word_len=[]
    for n in str:
        word_len.append((len(n),n))
    word_len.sort()
    return word_len[-1][1]
print(listCounter(["PHP","Exercise","Backend"]))

