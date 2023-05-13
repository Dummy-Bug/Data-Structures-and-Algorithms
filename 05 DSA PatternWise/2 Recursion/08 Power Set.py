#Function to return the lexicographically sorted power-set of the string.
def powerSet(s):
    
    result = []
    helper(s,len(s),result,"")
    
    result.sort()
    return result
    
def helper(s,n,result,path):# just save the path you are folowing 
                    # in the recurison tree and store it in result array.
    if n == 0 :
        result.append(path)
        return 
    
    include = helper(s,n-1,result,s[n-1] + path)
    exclude = helper(s,n-1,result,path)