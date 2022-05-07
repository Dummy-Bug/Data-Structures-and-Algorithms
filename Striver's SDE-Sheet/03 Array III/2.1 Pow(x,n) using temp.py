# https://www.codingninjas.com/codestudio/problems/1082146?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

def modularExponentiation(x, n, m):
	
	ans = 1
	while n!= 0:
		
		if n%2 == 0:
			x = (x*x)%m
			n = n//2
		else:
			ans = (ans*x)%m
			n   = n - 1
	return ans%m