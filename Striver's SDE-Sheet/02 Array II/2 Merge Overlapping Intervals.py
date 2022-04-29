# https://leetcode.com/problems/merge-intervals/

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


            
        