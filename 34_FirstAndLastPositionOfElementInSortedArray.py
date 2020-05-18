# Python3
# runtime: faster than 63.80% of submissions
# memory: less than 5.36% of submissions

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
        
            # locate index of first occurence in list
            first = nums.index(target)
            
            # locate index of last occurence in list using max() and enumerate()
            last = max(idx for idx, val in enumerate(nums)  if val == target) 
   
            return [first, last]
            
        # if target is not in the list, return [-1, -1]
        return [-1,-1]
