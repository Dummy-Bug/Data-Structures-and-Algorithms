### Problem description 

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
 

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
 

Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?


```

import heapq;

class MedianFinder:

    def __init__(self):
        self.min_heap = []; 
        self.max_heap = [];
        heapq.heapify(self.min_heap);
        heapq.heapify(self.max_heap);
    

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap,num);

        elif self.min_heap[0] <= num:
            heapq.heappush(self.min_heap,num);
        else:
            heapq.heappush(self.max_heap,-1*num);
        
        if len(self.min_heap)-len(self.max_heap) > 1:
            heapq.heappush(self.max_heap,-1*heapq.heappop(self.min_heap));
        
        elif len(self.max_heap)-len(self.min_heap) > 1:
            heapq.heappush(self.min_heap,-1*heapq.heappop(self.max_heap));
            
        

    def findMedian(self) -> float:
        # print(self.max_heap,self.min_heap);
        if ( len(self.max_heap) + len(self.min_heap) )%2 == 0:
            return ( -1*self.max_heap[0] + self.min_heap[0] )/2.0;
        
        elif len(self.max_heap)>len(self.min_heap):
            return -1*self.max_heap[0]*1.0;
        else:
            return self.min_heap[0]*1.0;
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

```
