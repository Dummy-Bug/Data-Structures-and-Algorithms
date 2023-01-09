### Problem Description

Given an array A of non-negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.



Problem Constraints
1 <= len(A) <= 100000
0 <= A[i] <= 2*109



Input Format
The first argument is an array of integers.



Output Format
Return a string representing the largest number.



Example Input
Input 1:

 A = [3, 30, 34, 5, 9]
Input 2:

 A = [2, 3, 9, 0]


Example Output
Output 1:

 "9534330"
Output 2:

 "9320"


Example Explanation
Explanation 1:

Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.
Explanation 2:

Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.


**Approach**

Sorting all numbers in descending order is the simplest solution that occurs to us. But this doesn’t work. 

For example, 548 is greater than 60, but in the output, 60 comes before 548. As a second example, 98 is greater than 9, 
but 9 comes before 98 in the output.

The solution is to use any comparison-based sorting algorithm. Thus, instead of using the default comparison, write a comparison 
function myCompare() and use it to sort numbers. 

Given two numbers, X and Y, how should myCompare() decide which number to put first – we compare two numbers XY (Y appended at the end of X) 
and YX (X appended at the end of Y). 

If XY is greater, then, in the output, X should come before Y, else Y should come before X. 

For example, let X and Y be 542 and 60. To compare X and Y, we compare 54260 and 60542. Since 60542 is greater than 54260, we put Y first.


```

class Solution:
    
    def compare(self,s1,s2):
        if s1+s2 < s2+s1:
            return 1;
        
        if s1+s2 == s2+s1:
            return 0;
        
        else:
            return -1

    def largestNumber(self, A):
        from functools import cmp_to_key;
        
        string_array = [];
        for i in range(len(A)):
            string_array.append(str(A[i]));
        
        # print(string_array)
        string_array.sort(key = cmp_to_key(self.compare));
        
        ans =  "".join(string_array);
        if ans[0] == '0':
            return '0'
        else:
            return ans



```
