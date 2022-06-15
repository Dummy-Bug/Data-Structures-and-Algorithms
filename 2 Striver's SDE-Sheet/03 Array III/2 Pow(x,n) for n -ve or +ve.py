# https://www.codingninjas.com/codestudio/problems/1082146?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

def modularExponentiation(x, n, m):
	
	return helper(x,n)%m
def helper(x,n):
	
	if n == 0:
		return 1
	elif n == 1:
		return x
	temp = 0 
	temp = helper(x,n//2)
	if n%2 == 0: # if even
		return (temp*temp)%m
	else:
		return (temp*temp*x)%m

# If N is allowed to be negative then whatever is the final answer
# then just return (1/ans)