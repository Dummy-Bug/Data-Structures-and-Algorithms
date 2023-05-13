### Problem Description 

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104


```

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        output = [intervals[0]]
        i = 1
        
        while i < len(intervals):
            
            if output[-1][1] >= intervals[i][0]: # compare last intervals y1 to current intervals x2
                               # lower limit will be x1 and upper limit will be max(y2,y1)
                output[-1]    = [output[-1][0],max(output[-1][1],intervals[i][1]) ] 
            
            else:# if not overlapping then simply append the interval
                 output.append(intervals[i])
            i = i + 1
        return output
        
        
```
