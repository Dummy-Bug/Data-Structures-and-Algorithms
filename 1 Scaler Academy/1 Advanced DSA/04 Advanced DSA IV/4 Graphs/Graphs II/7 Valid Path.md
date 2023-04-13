### Problem Description

There is a rectangle with left bottom as (0, 0) and right up as (x, y).

There are N circles such that their centers are inside the rectangle.

Radius of each circle is R. Now we need to find out if it is possible that we can move from (0, 0) to (x, y) without touching any circle.

Note : We can move from any cell to any of its 8 adjecent neighbours and we cannot move outside the boundary of the rectangle at any point of time.



Problem Constraints
0 <= x , y, R <= 100

1 <= N <= 1000

Center of each circle would lie within the grid



Input Format
1st argument given is an Integer x , denoted by A in input.

2nd argument given is an Integer y, denoted by B in input.

3rd argument given is an Integer N, number of circles, denoted by C in input.

4th argument given is an Integer R, radius of each circle, denoted by D in input.

5th argument given is an Array A of size N, denoted by E in input, where A[i] = x cordinate of ith circle

6th argument given is an Array B of size N, denoted by F in input, where B[i] = y cordinate of ith circle



Output Format
Return YES or NO depending on weather it is possible to reach cell (x,y) or not starting from (0,0).



Example Input
Input 1:

 x = 2
 y = 3
 N = 1
 R = 1
 A = [2]
 B = [3]
Input 2:

 x = 1
 y = 1
 N = 1
 R = 1
 A = [1]
 B = [1]


Example Output
Output 1:

 NO
Output 2:

 NO


Example Explanation
Explanation 1:

 There is NO valid path in this case
Explanation 2:

 There is NO valid path in this case
 
 
 **Solution Approach**
 
 Check if (i,j) is a valid point for all 0<=i<=x, 0<=j<=y. By valid point we mean that none of the circle should contain it.

To do this you can simply check for all points (i,j) where 0<=i<=x, 0<=j<=y if there is a circle on which this point.
If a point lies on a circle it should satisfy that circle’s equation.((i-a)^2+(j-b)^2==r^2 where (a,b) is the centre of the circle and r is its radius)

Now you know all the valid point in rectangle. You need to figure out if you can go from (0,0) to (x,y) through valid points. This can be done with any graph traversal algorithms like BFS/DFS.

DFS ( i , j )
mark (i,j) as visited
for all (i’,j’) positions to where we can travel to from (i,j)
DFS(i’,j’)

Now we just have to check if (x,y) is visited or not. If it is visited then output YES otherwise NO.
 
 ```
 
 
 import math
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def intersect_upper_half(self, i, j, r, x, y):
        if(i <= r):
            return True
        elif(j+r >= y):
            return True
        else:
            return False

    def intersect_lower_half(self, i, j, r, x, y):
        if(i+r >= x):
            return True
        elif(j <= r):
            return True
        else:
            return False

    def circle_intersect(self, i, j, x, y, r):
        distance = math.sqrt((x-i)**2 + (y-j)**2)
        if(distance <= 2*r):
            return True
        else:
            return False

    def check_circles(self, i, circles, visited):
        visited[i] = True
        if(self.intersect_lower_half(circles[i][0], circles[i][1], self.r, self.x, self.y)):
            return True
        else:
            for index in range(len(circles)):
                if(not visited[index]):
                    if(self.circle_intersect(circles[i][0], circles[i][1], circles[index][0], circles[index][1], self.r)):
                        ret_var = self.check_circles(index, circles, visited)
                        if(ret_var):
                            return True
            return False

    def solve(self, A, B, C, D, E, F):
        self.x = A
        self.y = B
        n = C
        self.r = D
        circles = [(a, b) for a, b in zip(E, F)]
        for i in range(n):
            if(self.intersect_upper_half(circles[i][0], circles[i][1], self.r, self.x, self.y)):
                ret_var = self.check_circles(i, circles, [False]*n)
                if(ret_var):
                    return "NO"
        return "YES"
        
 ```
