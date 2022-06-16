def sort_array(nums):
    
    if len(nums) == 0:
        return 
    
    temp = nums.pop() # storing the last element in temporary variable.
    # print(nums)
    sort_array(nums)
    
    insert(nums,temp) # call function to store the variable in it's right position.
    
    return 

def insert(nums,temp):
    
    if len(nums) == 0 or nums[-1] <= temp: # if last element is smaller just append the temp.
        nums.append(temp)
        return 
        
    element = nums.pop()
    
    insert(nums,temp) # call insert for the smaller input.
    
    nums.append(element) # add the element to nums after placing temp in it's position.
    
    return 

arr = [2,3,7,6,4,5,9]

sort_array(arr)

print(arr)