'''
    Time Complexity: O(N)
    Space complexity: O(1)
    
    Where N is the length of the array.
'''

def flipBits(arr, n):
    totalOnes = 0

    # Initialize overall maximum difference for any subArray
    maxVal = 0
    
    # Initialize current difference
    currMax = 0
    for i in range(n):
        if (arr[i] == 1): 
            totalOnes += 1
            
        # Value to be considered for finding maximum sum
        val = 0
        if (arr[i] == 1):
            val = -1
        else:
            val = 1
            
        currMax = max(val, currMax + val)
        maxVal = max(maxVal, currMax)
    
    maxVal = max(0, maxVal)
    result = totalOnes + maxVal
    return result