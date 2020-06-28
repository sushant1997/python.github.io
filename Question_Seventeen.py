#17. Write a Python program to multiplies all the items in a list

def mul_list(item):
    total = 1
    for i in item:
        total *=i
    return total
    
print(mul_list([2,3,4,5,10]))    