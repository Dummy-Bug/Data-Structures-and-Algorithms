### Merge Intervals

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary)


https://www.interviewbit.com/problems/merge-intervals/


**Hint**
This problem has a lot of corner cases which need to be handled correctly.

Let us first talk about the approach.
Given all the intervals, you need to figure out the sequence of intervals which intersect with the given newInterval.

Lets see how we check if interval 1 (a,b) intersects with interval 2 (c,d):

Overlap case :

    a---------------------b                      OR       a------b
                c-------------------d                c------------------d
Non overlap case :

    a--------------------b   c------------------d
Note that if max(a,c) > min(b,d), then the intervals do not overlap. Otherwise, they overlap.

Once we figure out the intervals ( interval[i] to interval[j] ) which overlap with newInterval, note that we can replace all the overlapping intervals with one interval which would be

(min(interval[i].start, newInterval.start), max(interval[j].end, newInterval.end)).

Do make sure you cover the other corner cases


### Solution Approach

Have you covered the following corner cases :

1) Size of interval array as 0.

2) newInterval being an interval preceding all intervals in the array.

    Given interval (3,6),(8,10), insert and merge (1,2)
3) newInterval being an interval succeeding all intervals in the array.

    Given interval (1,2), (3,6), insert and merge (8,10)
4) newInterval not overlapping with any interval and falling in between 2 intervals in the array.

    Given interval (1,2), (8,10) insert and merge (3,6) 
5) newInterval covering all given intervals.

    Given interval (3, 5), (7, 9) insert and merge (1, 10)
    
 **First consider the cases that are not overlapping**
 
 ```
 
 
 # Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):

        result = [];

        for i in range(len(intervals)):

            if newInterval.start > intervals[i].end :
                result.append(intervals[i]);

            elif newInterval.end < intervals[i].start :

                result.append(newInterval);

                for i in range(i,len(intervals)):
                    result.append(intervals[i]);
                return result;
            
            else:
                newInterval.start = min(newInterval.start,intervals[i].start);
                newInterval.end   = max(newInterval.end,intervals[i].end);
        else:
            result.append(newInterval);
        
        return result



 
 ```
