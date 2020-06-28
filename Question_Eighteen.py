# 18. Write a Python program to get the largest number from a list.


def list_compare(list):
    container=list[0]
    for i in list:
        if i > container:
            container=i
    return container
print(list_compare([1,2,3,40,60,80]))


