class Solution:
    
    def sorted(self, s):
        
        if len(s) == 0 :
            return 
        
        temp = s.pop() # pop out the last item
        
        self.sorted(s) # call the function using smaller input
        
        self.insert(s,temp) # insert the popped item to it's right position.
        
        return
    
    def insert(self,s,element):
        
        if len(s) == 0 or s[-1] > element:
            
            s.append(element)
            return
        
        temp = s.pop() # pop till element is > than it's elements to the left of it.
        
        self.insert(s,element)
        
        s.append(temp) # insert all the elements that were popped out.
        
        return