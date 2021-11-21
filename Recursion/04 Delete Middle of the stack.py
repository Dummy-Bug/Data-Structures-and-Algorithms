
class Solution:

    def deleteMid(self, s, sizeOfStack):
        
        import math
        
        if len(s) == math.ceil(sizeOfStack/2):
            s.pop()
            return
        
        temp = s.pop() # pop elements till we hit the middle 
        
        self.deleteMid(s,sizeOfStack)
        
        s.append(temp)