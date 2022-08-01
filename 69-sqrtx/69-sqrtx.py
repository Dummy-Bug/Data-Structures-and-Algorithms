class Solution:
    def mySqrt(self, A: int) -> int:
        
        low  = 0;
        high = A;
        candidate = 1;
        
        while low <= high:
            
            mid = low + (high-low)//2;
            
            squared_mid = mid*mid;
            
            if squared_mid == A:
                return mid;
            
            if squared_mid < A:
                candidate = mid;
                low = mid + 1;
            else:
                high = mid - 1;
        
        return candidate; 