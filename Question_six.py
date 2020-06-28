"""

6. Write a Python program to find the first appearance of the substring 'not' and
'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'

"""
def sampleString(str):
    remove_not = str.find('not')
    add_other = str.find('poor')
    
    if add_other > remove_not and remove_not>0 and add_other>0:
        str = str.replace(str[remove_not:(add_other+4)],'good')
        return str
    else:
        return str
print(sampleString('the lyric is not that poor!'))
print(sampleString('the lyric is poor!'))
