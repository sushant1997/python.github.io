#  19.Write a Python program to get the smallest number from a list

def smallest_list_num(list):
    container = list[0]
    for i in list:
        if i< container:
            container=i
        
    return container
    
print(smallest_list_num([1,2,3,4,50,70]))