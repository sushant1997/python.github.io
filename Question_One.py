 #"""1. Write a Python program to count the number of characters (characterfrequency) in a string. Sample String : google.com'
 #Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""



def word_count(str):
    dict={}
    for n in str:
        keys=dict.keys()
        if n in keys: 
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(word_count('google.com'))