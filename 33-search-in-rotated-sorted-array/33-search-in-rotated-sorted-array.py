class Solution:
    def search(self, A: List[int], B: int) -> int:
        low  = 0;
        high = len(A)-1;
        
        while low <= high :
            
            mid = low + (high-low)//2;
            
            if A[mid] == B:
                return mid;
                
            if A[low] <= A[mid]:
                
                if A[low] <= B and B <= A[mid]:
                    high = mid - 1;
                else:
                    low  = mid + 1; 
            else:
                if A[mid] <= B and B <= A[high]:
                    low = mid + 1;
                else:
                    high = mid - 1
        return -1