"""\
# 13. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red

"""


item = input("input comma separated value:")
words = [word for word in item.split(",")]
print(",".join(sorted(list(set(words)))))