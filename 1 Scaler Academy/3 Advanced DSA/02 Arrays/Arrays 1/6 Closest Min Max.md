### Closest MinMax

Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array.

**Notes**

**Approach 1**

> In first approach just check if A[i] is minimum or maximum, say we encounter minimum.
> After that run another loop starting from i+1 , if encounter the max then update the size 
> This solution is O(n);

```
class Solution:

    def solve(self, A):

        minimum , maximum = float('inf'),float('-inf')

        for i in range(len(A)):

            minimum = min(minimum,A[i])
            maximum = max(maximum,A[i])
        
        # print(minimum,maximum)
        if minimum == maximum:
            return 1

        i = 0; 
        size = float('inf'); mini = maxy = False
        while i < len(A):

            if A[i] == minimum:
                mini = True
            
            elif A[i] == maximum:
                maxy = True
            
            else:
                i = i + 1
                continue

            for j in range(i+1,len(A)):

                if mini:
                    if A[j] == minimum:
                        i = j                    
                    if A[j] == maximum:

                        size = min(size,j-i+1)
                        i = j 
                        break

                if maxy:
                    
                    if A[j] == maximum:
                        i = j
                    if A[j] == minimum:
                        size = min(size,j-i+1)
                        i = j 
                        break
            else:
                i = i + 1
            mini = maxy = False
        return size
```

**Approach 2**

>  keep track of every last occurrence of the minimum and maximum element of the array.
> In order to find the start point, we can simply remember the last occurrences of a minimum and a maximum value, respectively. And for each 
> min-max pair, we check the length of the subarray that encloses them and then update out overall based on that.

```
class Solution:

    def solve(self, A):

        latest_min_ptr = -1;
        latest_max_ptr = -1;
        min_val = max_val = A[0];

        for i in range(1,len(A)):

            min_val = min(min_val,A[i]);
            max_val = max(max_val,A[i]);

        size = len(A);

        for i in range(len(A)):
            
            if A[i] == min_val:
                latest_min_ptr = i;
            
            if A[i] == max_val:
                
                latest_max_ptr = i;

            
            if latest_max_ptr !=-1 and latest_min_ptr !=-1 :

                size = min(size,abs(latest_max_ptr-latest_min_ptr)+1)
            
        return size;

```
