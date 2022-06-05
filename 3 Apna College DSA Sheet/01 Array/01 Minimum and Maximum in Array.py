# https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1/#
def getMinMax( a, n):
    
    maximum = minimum = a[0]
    
    for i in range(1,n):
        maximum = max(maximum,a[i])
        minimum = min(minimum,a[i])
    
    return [minimum,maximum]