"""
25. Write a Python program to check whether all dictionaries in a list are empty or not.
Sample list : [{},{},{}]
Return value : True
Sample list : [{1,2},{},{}]
Return value : False
"""

my_list= [{},{},{}]
my_list1=[{2,1},{},{}]
print(all(not d for d in my_list1))
print(all(not d for d in my_list))