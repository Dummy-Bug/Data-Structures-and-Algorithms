class Solution:
    def totalFruit(self, fruits: List[int]):
        
        dx = dict()
        unique_fruits, result, i = 0, 0, 0
        
        for j in range(len(fruits)):
            fruit = fruits[j]
            
            if fruit not in dx or dx[fruit] == 0:
                dx[fruit] = 0
                unique_fruits += 1
                
            dx[fruit] += 1
            
            if unique_fruits < 2:
                result = max(result,j-i+1)
                j = j + 1
                
            elif unique_fruits == 2:
                result = max(result,j-i+1)
                j = j + 1
            
            else:
                while unique_fruits > 2 :
                    
                    fruit = fruits[i]
                    dx[fruit] -= 1
                    
                    if dx[fruit] == 0:
                        unique_fruits -= 1
                        
                    i = i + 1
                j = j + 1
        return result
                
        