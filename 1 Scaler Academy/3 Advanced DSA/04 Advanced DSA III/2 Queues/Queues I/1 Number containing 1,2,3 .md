### Problem Description

Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.

NOTE: All the A integers will fit in 32-bit integers.



Problem Constraints
1 <= A <= 29500



Input Format
The only argument given is integer A.



Output Format
Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.



Example Input
Input 1:

 A = 3
Input 2:

 A = 7


Example Output
Output 1:

 [1, 2, 3]
Output 2:

 [1, 2, 3, 11, 12, 13, 21]


Example Explanation
Explanation 1:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.
Explanation 2:

 Output denotes the first 3 integers that contains only digits 1, 2 and 3.

**Approach**
We know the initial three values will be 1, 2, and 3.

Now, the upcoming values will be by appending 1, 2, and 3 in each given value.

We will use a queue to store the elements in ascending order.

```

from collections import deque;

class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):

        q = deque();

        q.append('1');q.append('2');q.append('3');

        num_delete = 0; result = [];
        count = 3;
        while count < A:

            string = q.popleft();
            num_delete += 1;
            result.append(int(string));
            q.append(string+'1');
            q.append(string+'2');
            q.append(string+'3');
            count += 3;
        
        while num_delete < A:
            string = q.popleft();
            result.append(int(string));
            num_delete += 1;
        return result;


```


**Better Approach**


```

from collections import deque
class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        ans = []
        q = deque()
        q.append(1)
        q.append(2)
        q.append(3)
        cnt = 3
        while len(ans) < A:
            x = q.popleft()
            ans.append(x)
            if cnt>=A: 
                continue
            # append 1, 2 and 3 to the current number
            x1 = x * 10 + 1
            x2 = x * 10 + 2
            x3 = x * 10 + 3
            q.append(x1)
            q.append(x2)
            q.append(x3)
            cnt += 3
        return ans
    
    
    ```
