# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1#
class Solution:
    #Function to find next gap.
    def nextGap(self,gap):
        
        #It returns the ceil value of gap/2 or 0 if gap is 1.
        if(gap<=1):
            return 0
        return ((gap+1)//2)
        
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        gap=n+m
        gap = self.nextGap(gap)
        while(gap>0):
            i=0
            
            #Comparing elements in the first array itself with difference in 
    	    #index equal to the value of gap.
            while(i+gap<n):
                
                #If element at ith index is greater than element at
    		    #(i+gap)th index, we swap them.
                if(arr1[i]>arr1[i+gap]):
                    arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
                i+=1
    
            j = max(0, gap - n)
            
            #Now comparing elements in both arrays with help of two pointers.
    		#The loop stops whenever any pointer exceeds the size of its array.
            while(i<n and j<m):
                
                #If element in the first array is greater than element in
    		    #second array, we swap them.
                if(arr1[i]>arr2[j]):
                    arr1[i],arr2[j]=arr2[j],arr1[i]
                i+=1
                j+=1
        
            if(j<m):
                j=0
                
                #At last, comparing elements in the second array itself with 
                #difference in index equal to the value of gap.
                while(j+gap < m):
                    
                    #If element at jth index is greater than element at
    		        #(j+gap)th index, we swap them.
                    if (arr2[j] > arr2[j + gap]):
                        arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                    j+=1
                    
            #Updating the value of gap.        
            gap = self.nextGap(gap)