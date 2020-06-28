# 16.Write a Python program to sum all the items in a list

def total_sum_list(item):
    sum_num=0
    for i in item:
        sum_num +=i
    return sum_num
    
print (total_sum_list([2,3,4,5,6,7,8]))