class Solution:
	def slidingMaximum(self,arr,k):
        if len(arr) <= 1:
            return arr
		from collections import deque
		dq = deque([])
		result = []
		i = 0
		for j in range(len(arr)):
		    while dq and dq[-1] < arr[j]: # removing unnecessary elements.
		        dq.pop()
		        
		    dq.append(arr[j])
		    if j < k-1:
		        j = j + 1
		        continue
		        
		    if dq[0] == arr[i]:
		        result.append(dq.popleft())
		    else:
		        result.append(dq[0])
		    i = i + 1
		return result

