def printFirstNegativeInteger(arr, n, k):
    
    from collections import deque
    q = deque()
    result = []
    i = 0
    for j in range(k):
        if arr[j] < 0: # storing all the -ve values of first window
            q.append(arr[j])
            
    while j < n:
        if not q: # if q is empty 
            result.append(0)
        else:
            if arr[i] == q[0]:
                result.append(q.popleft())
            else:
                result.append(q[0])
        j = j + 1
        i = i + 1
        if  j < n and arr[j] < 0 :
            q.append(arr[j])
    
    return result