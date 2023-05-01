### Problem Description

Given two arrays of integers A and B, Sort A in such a way that the relative order among the elements will be the same as those are in B.
For the elements not present in B, append them at last in sorted order.

Return the array A after sorting from the above method.

NOTE: Elements of B are unique.



Problem Constraints
1 <= length of the array A <= 100000

1 <= length of the array B <= 100000

-10^9 <= A[i] <= 10^9



Input Format
The first argument given is the integer array A.

The second argument given is the integer array B.



Output Format
Return the array A after sorting as described.



Example Input
Input 1:

A = [1, 2, 3, 4, 5]
B = [5, 4, 2]
Input 2:

A = [5, 17, 100, 11]
B = [1, 100]


Example Output
Output 1:

[5, 4, 2, 1, 3]
Output 2:

[100, 5, 11, 17]


Example Explanation
Explanation 1:

 Simply sort as described.
Explanation 2:

 Simply sort as described.


**Approach**

Loop through A, store the count of every number in a HashMap (key: number, value: count of number).
Loop through B, check if it is present in HashMap, put in the output array as many times in A,
and remove the number from HashMap.
Sort the rest of the numbers in HashMap and put them in the output array.


```

class Solution:

    def solve(self, A, B):

        freq_map = dict();
        st       = set();
        sorted_order = [];

        for num in A:
            if num not in freq_map:
                freq_map[num] = 0;
            freq_map[num] += 1;
        
        A.sort();

        for num in B:
            if num in freq_map:
            
                while freq_map[num] !=0:
                    freq_map[num] -= 1;
                    sorted_order.append(num);
            st.add(num);
        
        for num in A:
            if num not in st:
                sorted_order.append(num);
        
        return sorted_order;
        
```
