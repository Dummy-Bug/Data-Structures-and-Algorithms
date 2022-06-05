# https://practice.geeksforgeeks.org/problems/reverse-a-string/1#

def reverseWord(s):

    result = ''
    
    for i in range(len(s)-1,-1,-1):
        result = result + s[i]
        
    return result