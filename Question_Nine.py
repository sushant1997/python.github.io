# 9. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def changeChar(a):
    str1 = a[-1:]+a[1:-1]+a[:1]
    return str1

print(changeChar('abcd'))

    