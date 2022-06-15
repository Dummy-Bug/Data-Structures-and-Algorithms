# https://www.codingninjas.com/codestudio/problems/1062679?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=1
def findNthRootOfM(n,m):
 
    low = 1
    high = m
    eps = 1e-7
    while high-low>eps:
        
        mid = (high+low)/2.0
        
        if pow(mid,n) < m:
            low = mid 
        else:
            high = mid
    return '%0.6f' %high