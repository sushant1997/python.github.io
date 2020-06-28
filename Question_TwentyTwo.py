# 22.Write a Python program to remove duplicates from a list

def remove_duplicate(sets):
    dup_item=set()
    unique_item=[]
    for x in sets:
        if x not in dup_item:
            unique_item.append(x)
            dup_item.add(x)

        return unique_item


print(remove_duplicate([10,20,30,40,50,20,30,60]))

"""
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
"""