# https://www.codingninjas.com/codestudio/guided-paths/data-structures-algorithms/content/118820/offering/1381873?leftPanelTab=0


'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is the size of array/list.
'''


def kadane(arr, n, k):
    maxSum = -1e9
    curSum = 0

    for i in range(n*k):
        curSum += arr[i % n]

        maxSum = max(maxSum, curSum)

        if curSum < 0:
            curSum = 0

    return maxSum


def maxSubSumKConcat(arr, n, k):

    maxSubSum = -1

    if k == 1:
        maxSubSum = kadane(arr, n, k)

        return maxSubSum


    arrSum = 0

    for i in range(n):
        arrSum += arr[i]

    if arrSum <= 0: 
        # Finding the maximum subarray sum for k = 2 
        maxSubSum = kadane(arr, n, 2)
    else:
        # Finding the maximum subarray sum for k = 2, 
        maxSubSum = kadane(arr, n, 2)
        maxSubSum += (k - 2) * arrSum
        
#         we cannot do (k-1)*arrSum + kadane(arr,n,1) run it to see why

    return maxSubSum