"""
3. Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t
"""

def change(str):
    str=input("enter word:")
    char= str[0]
    str=str.replace(char,'$')
    str= char +str[1:]
    return str

print(change(str))