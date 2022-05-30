# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#

class Solution:
    def maximumMeetings(self,n,start,end):
        
        meetings = []
        
        for i in range(len(start)):
            meetings.append([start[i],end[i]])
        
        meetings = sorted(meetings,key = lambda x:x[1])
        # print(meetings)
        result = 1
        prev_end_time = meetings[0][1]
        for i in range(1,len(start)):
            
            start_time = meetings[i][0]
            end_time   = meetings[i][1]
            
            
            
            if prev_end_time < start_time:
                result += 1
                prev_end_time = meetings[i][1]
        
        return result