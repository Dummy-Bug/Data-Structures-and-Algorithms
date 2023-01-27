### Problem Description

We have a list A of points (x, y) on the plane. Find the B closest points to the origin (0, 0).

Here, the distance between two points on a plane is the Euclidean distance.

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in.)

NOTE: Euclidean distance between two points P1(x1, y1) and P2(x2, y2) is sqrt( (x1-x2)2 + (y1-y2)2 ).



Problem Constraints
1 <= B <= length of the list A <= 105
-105 <= A[i][0] <= 105
-105 <= A[i][1] <= 105



Input Format
The argument given is list A and an integer B.



Output Format
Return the B closest points to the origin (0, 0) in any order.



Example Input
Input 1:

 A = [ 
       [1, 3],
       [-2, 2] 
     ]
 B = 1
Input 2:

 A = [
       [1, -1],
       [2, -1]
     ] 
 B = 1


Example Output
Output 1:

 [ [-2, 2] ]
Output 2:

 [ [1, -1] ]


Example Explanation
Explanation 1:

 The Euclidean distance will be sqrt(10) for point [1,3] and sqrt(8) for point [-2,2].
 So one closest point will be [-2,2].
Explanation 2:

 The Euclidean distance will be sqrt(2) for point [1,-1] and sqrt(5) for point [2,-1].
 So one closest point will be [1,-1].
 
 **Approach**
 
 Sort the list of these points with respect to the distance from the origin. 
We can do this with the help of a comparator function, which takes two elements of the array as input 
and returns which one will be smaller than the other. So basically, it takes care of the comparison process.

After the list is sorted, take the first B elements from the list and create a new list and return it. 
Think of calculating the Euclidean distance and storing it efficiently.

Time Complexity - O(N log N)
Space Complexity - O(N)

 
 ```
 
 from functools import cmp_to_key
def dist(x):
    return (x[0] * x[0]) + (x[1] * x[1])
def compare(item1, item2):
    if dist(item1) < dist(item2):
        return -1
    elif dist(item1) > dist(item2):
        return 1
    else:
        return 0
class Solution:
    def solve(self, A, B):
        ans = []
        A = sorted(A, key = cmp_to_key(compare))
        for i in range(B): 
            ans.append(A[i])
        return ans
 
 ```
