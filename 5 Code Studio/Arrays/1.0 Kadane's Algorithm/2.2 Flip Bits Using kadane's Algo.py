# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381872?leftPanelTab=1

def flipBits(arr, n):
    totalOnes = 0; maxVal = 0; currMax = 0
    
    for i in range(n):
        if (arr[i] == 1): 
            totalOnes += 1
        val = 0
        if (arr[i] == 1):
            val = -1
        else:
            val = 1
        currMax += val;
        maxVal = max(maxVal, currMax)
        
        if currMax < 0:
            currMax = 0
    
    maxVal = max(0, maxVal)
    result = totalOnes + maxVal
    return result
            
            
                    
    