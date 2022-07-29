### Add One to Very Large Number

https://leetcode.com/problems/plus-one/ 

<hr>

**Notes**
> Trivial Question
<hr>

```

class Solution:

    def plusOne(self, A):

        carry = 1

        for i in range(len(A)-1,-1,-1):

            if carry == 0:# if carry gets zero in the middle just 
                          
                for i in range(len(A)):
                    if A[i] != 0:
                        return A[i:]
            
            carry,A[i] = divmod(A[i]+carry,10);
        
        if carry == 1:
            A.insert(0,1)
            return A
        
        if carry == 0:
        for i in range(len(A)):

            if A[i] != 0:
                return A[i:]

```
