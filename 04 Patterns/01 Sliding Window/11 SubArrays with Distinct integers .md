### Problem Description

Given an array A of positive integers,call a (contiguous,not necessarily distinct) subarray of A good if the number of different 
integers in that subarray is exactly B.

(For example: [1, 2, 3, 1, 2] has 3 different integers 1, 2 and 3)

Return the number of good subarrays of A.

https://www.interviewbit.com/problems/subarrays-with-distinct-integers/

Problem Constraints
1 <= |A| <= 40000

1 <= A[i] <= |A|

1 <= B <= |A|



Input Format
The first argument given is the integer array A.

The second argument given is an integer B.



Output Format
Return an integer denoting the number of good subarrays of A.



Example Input
Input 1:

 A = [1, 2, 1, 2, 3]
 B = 2
Input 2:

 A = [1, 2, 1, 3, 4]
 B = 3


Example Output
Output 1:

 7
Output 2:

 3


Example Explanation
Explanation 1:

  Subarrays formed with exactly 2 different integers: [1, 2], [2, 1], [1, 2], [2, 3], [1, 2, 1], [2, 1, 2], [1, 2, 1, 2].
Explanation 2:

  Subarrays formed with exactly 3 different integers: [1, 2, 1, 3], [2, 1, 3], [1, 3, 4].
  
  
  **Approach**
  
  * Total num subarrays = subarrays with less than B distinct elements + subarrays with greater than B distinct elements + num subarrays with exactly B distinct elements

* Thus S = a+b+c;
using two pointers it is easy to find a and b and we have formula for S already so just solve
c = S-(a+b);

OR

we can also find

num subarrays with less than eqal to B = num subarrays with less than B + num subarrays with exactly equal to B;

S = A+B;

it is easier to find S and A Hence 
B = S-A;



** In official solution they have used the 2nd method 

if we further optimize it we can do this with using only one fucntion.

bcz distinct_elementsl_less than B is nothing but distinct element less tha equal to B-1

so call the same function with B and B-1 and find the difference to get the last answer.

```


class Solution:

    def solve(self, A, B):
        return self.helper(A,B)-self.helper(A,B-1);
        
    def helper(self,A,B):

        freq_map = dict();
        distinct_count = 0 ; result = 0
        
        p1 = p2 = 0; 
        
        for i in range(len(A)):
            freq_map[A[i]] = 0;
        
        # read the notes 
        
        while p2 < len(A):
            
            freq_map[A[p2]] += 1;
            
            if freq_map[A[p2]] == 1:
                distinct_count += 1;
            
            if distinct_count <= B:
                result += p2-p1+1;
                p2 += 1;
            else:
                while distinct_count > B:
                    freq_map[A[p1]] -= 1;
                    
                    if freq_map[A[p1]] == 0:
                        distinct_count -= 1;
                    p1 += 1;
                
                result += p2-p1+1;
                p2 += 1;
                
        return result;

        

```
