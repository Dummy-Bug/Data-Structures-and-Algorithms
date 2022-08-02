### Merge overlapping Intervals

* Given a collection of intervals, merge all overlapping intervals.

https://www.interviewbit.com/problems/merge-overlapping-intervals/


### Solution Approach

Given all the intervals, you need to figure out the sequence of intervals which intersect.

Lets see how we check if interval 1 (a,b) intersects with interval 2 (c,d):

Overlap case :

a---------------------b          OR             a------b
            c-------------------d           c------------------d
Nonoverlap case :

a--------------------b   c------------------d
If max(a,c) > min(b,d), then the intervals do not overlap. Otherwise, they overlap.

Do you think it will be easier to solve if you could sort the intervals based on the starting point?

First lets sort the array based on the starting point , if starting points are equal then based on ending point.
We can maintain two variables cur_start and cur_end where cur_start is the left most point of the current segment and cur_end is rightmost point of the current segment.
Set cur_start to the starting point of the first element and cur_end to the ending point of the first element.

Now we iterate from 1 to n-1 and for every i we check the following
if A[i].left <= cur_end
This means i’th interval overlapps with the current interval, so we can add this to the current interval
else
This means the i’th interval doesnt overlapp with the current interval, therefore we can add the current interval to our answer and make a new interval i.e. set cur_start=A[i].start and cur_end=A[i].end

Lastly dont forget to add the current interval to our answer.


```

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        
        intervals.sort(key = lambda x:x.start)
        result = [intervals[0]];

        for i in range(1,len(intervals)):
            
            if result[-1].end < intervals[i].start:
                result.append(intervals[i]);
                continue
            
            result[-1].start = min(result[-1].start,intervals[i].start);
            result[-1].end   = max(result[-1].end,intervals[i].end);
        
        return result;



```
