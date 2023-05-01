### Problem Description 

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points
to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 

Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
Accepted
942,067
Submissions
1,431,250


**T(c) = O(Nlog(k));**

```

import heapq;

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []; k = k-1; result = [];
        
        for x,y in points:
            
            dist = (x**2+y**2)**0.5;
            
            if len(heap) <= k:
                heapq.heappush(heap,[-1*dist,[x,y]]);
                continue;
            if -1*heap[0][0] > dist:
                heapq.heappop(heap);
                heapq.heappush(heap,[-1*dist,[x,y]]);
            
        while len(heap) != 0:
            dist,points = heapq.heappop(heap);
            
            result.append(points);
        
        return result;
        
```

**Quick Select**

```

class Solution:
    def kClosest(self, nums: List[List[int]], k: int) -> List[List[int]]:
        
        self.k = k-1; start = 0; end = len(nums)-1;
        
        while start <= end:
            
            pivot_index = random.randint(start,end);
            pivot_index = self.partition(nums,start,end,pivot_index)

            if pivot_index == self.k:
                return nums[:pivot_index+1];
            elif pivot_index > self.k:
                end = pivot_index - 1;
            else:
                start = pivot_index + 1;
    
    def partition(self,points,start,end,pivot_index):
        
        points[start],points[pivot_index]=points[pivot_index],points[start];
        pivot = start; left = start+1;right = end;
        
        while left<=right:
            
            if points[left][0]**2+points[left][1]**2 <= points[pivot][0]**2+points[pivot][1]**2:
                left += 1;
            elif points[right][0]**2+points[right][1]**2 > points[pivot][0]**2+points[pivot][1]**2:
                right -= 1;
            else:
                points[left],points[right] = points[right],points[left];
                left += 1;
                right -= 1;
        points[left-1],points[pivot] = points[pivot],points[left-1];
        
        return left-1;

```
