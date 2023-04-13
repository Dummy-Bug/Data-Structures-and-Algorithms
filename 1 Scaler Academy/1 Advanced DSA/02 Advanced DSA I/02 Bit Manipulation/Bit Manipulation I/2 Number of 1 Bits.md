### Problem Description

Write a function that takes an integer and returns the number of 1 bits it has.

```

class Solution:

    def numSetBits(self, A):

        count = 0;

        for i in range(32):
            if self.SetBit(A,i):
                count += 1;
        
        return count
    
    def SetBit(self,num,n):
        if (num>>n)&1 == 1:
            return 1;
        return 0;


```

```

class Solution:

    def numSetBits(self, A):

        count = 0;

        while A > 0:

            if A&1 == 1:
                count += 1;
            
            A = A>>1;
        
        return count

```
