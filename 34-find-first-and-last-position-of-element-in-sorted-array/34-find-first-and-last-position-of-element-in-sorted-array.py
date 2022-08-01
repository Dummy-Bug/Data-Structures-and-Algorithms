class Solution:
    def searchRange(self, A: List[int], B: int) -> List[int]:
        
        left_index  = self.lowerbound(A,B);
        right_index = self.upperbound(A,B);
        
        return [left_index,right_index];
        
    def lowerbound(self,A,B):
        
        low = 0; high = len(A)-1;
        index = -1;
        
        while low <= high:
            
            mid = low + (high-low)//2;
            
            if A[mid] == B:
                index = mid;
                high  = mid - 1;
                
            elif A[mid] < B:
                low = mid + 1;
            
            else:
                high = mid - 1;
        
        return index    
    
    def upperbound(self,A,B):
        
        low = 0; high = len(A)-1;
        index = -1;
        
        while low <= high:
            
            mid = low + (high-low)//2;
            
            if A[mid] == B:

                index = mid;
                low = mid + 1;
                
            elif A[mid] <= B:
                
                low = mid + 1
            else:
                high = mid - 1;
        
        return index;
        