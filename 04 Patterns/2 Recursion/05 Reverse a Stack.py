def reverse_stack(s):
    
    if not s:
        return
    
    top = s.pop()
    
    reverse_stack(s)
    
    insert(s,top)
    
def insert(s,ele):
    
    if not s : 
        s.append(ele)
        return 
    top = s.pop() # pop all the elements so that we can insert the element in its' right position.
    
    insert(s,ele)
    
    s.append(top) # append all the popped elements
    
stack = [1,2,3,4,5]

reverse_stack(stack)

print(stack)