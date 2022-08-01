### Rain Water Trapped 

https://leetcode.com/problems/trapping-rain-water/

**Hint**

* Take a close look at any particular bin. How high can this hold water? If you can compute the answer to the above question for every bin, you are done.

* Every bin will store water which will depend on some prefix and suffix quantity.



### Approach 1
* Instead of calculating area by height*width, we can think it in a cumulative way.
* In other words, we can sum the water amount of each bin(width=1).

> We can keep 2 arrays ‘pre’ and ‘suf’. pre[i] is the maximum height for all i from 0 to i and suf[i] is the maximum height for all i from i to n-1.
> Now for each i from 1 to n-2 (as no water can be stored at indexes 0 and 1) just add the maximum amount water that can be stored. The maximum amount of water that can be stored is the minimum of(max height towards left of i,max height towards right of i)-A[i]
> i.e. min(pre[i-1],suf[i+1])-A[i]. But if min(pre[i-1],suf[i+1])-A[i]<0 we dont add anything. (i.e we add 0)



```

class Solution:

	def trap(self, A):

		total_water_trapped = 0;
		left_max = [A[0]];
		right_max = [A[-1]]*len(A);
		n = len(A);

		for i in range(1,n):
			left_max.append(max(left_max[-1],A[i]));
		
		for i in range(n-2,-1,-1):
			right_max[i] = max(right_max[i+1],A[i]);

		for i in range(1,n-1):

			water_trapped = min(left_max[i],right_max[i]) - A[i];

			if water_trapped > 0:
				total_water_trapped += water_trapped;
		
		return total_water_trapped



```

**More Efficient soltuion without using constant space only is also possible**
