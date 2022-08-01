### First Missing Integer


https://www.interviewbit.com/problems/first-missing-integer/

**Hints**


To simply solve this problem, search all positive integers, starting from 1 in the given array. We may have to search at most n+1 numbers in the given array. So this solution takes O(n^2) in the worst case.

We can use sorting to solve it in lesser time complexity. We can sort the array in O(NlogN) time.

Once the array is sorted, then a linear scan of the array is all that remains to be done.

So this approach takes O(nLogn + n) time which is O(nLogn).

We can also use hashing. We can build a hash table of all positive elements in the given array.

Once the hash table is built, all positive integers, starting from 1 can be searched here. As soon as we find a number that is not there in the hash table, we return it.

Approximately, this approach may take O(n) time, but it requires O(n) extra space.

But what we are really looking for is a O(n) time, O(1) space solution.

Note that ( N being the size of the array ), A[i]<=0 and A[i]>N are not the numbers you are looking for because the missing positive integer will be in the range [1, N+1].

The answer will be N+1 if and only if all of the elements of the array have exactly one occurrence of [1, N].

If using extra space was an option, creating buckets would have been an easy solution.

Creating an array of size N initialized to 0, for every value A[i], which lies in the range [1, N], we would have incremented its count in the array. Consequently, we would traverse the array to find the first array position with value 0, hence finding our answer.

However, since we are not allowed buckets, can we use the existing array as a bucket somehow?



### Solution Approach

Note: numbers A[i]<=0 and A[i]>N ( N being the size of the array ) are not important to us since the missing positive integer will be in the range [1, N+1].

The answer will be N+1 only if all of the elements of the array are exact one occurrence of [1, N].

Creating buckets would have been an easy solution if using extra space was allowed.

An array of size N initialized to 0 would have been created.

For every value A[i], which lies in the range [1, N], its count in the array would have been incremented.

Finally, traversing the array would help to find the first array position with value 0, and that will be our answer.
However, usage of buckets is not allowed; can we use the existing array as a bucket somehow?

Now, since additional space is not allowed either, the given array itself needs to be used to track it.

It may be helpful to use the fact that the size of the set we are looking to track is [1, N]

which happens to be the same size as the size of the array.

This means we can use the array to track these elements.

We traverse the array, and if A[i] is in [1, N] range, we try to put in the index of same value in the array.

Time complexity : O(n)
Auxiliary Space : O(1)

```

class Solution:

    def firstMissingPositive(self, A):

        for i in range(len(A)):
            
            while(A[i]>0 and A[i] < len(A) and A[i] != A[A[i]-1]):

                A[A[i]-1],A[i] = A[i],A[A[i]-1]; 

        for i in range(len(A)):
            
            if A[i] != i+1:
                return (i+1);
        
        return len(A)+1;
            
                  

```
