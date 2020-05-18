# Python3

# solution 1
# runtime: faster than 10.49% of submissions
# memory: less than 5.97% of submissions

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # add the target into nums if not there and sort
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
        
# solution 2
# runtime: faster than 11.18% of submissions
# memory: less than 5.97% of submissions

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        # iterate over indexes until we find element at index that is greater than target
        for i in range(len(nums)):
            if nums[i] > target:  
                return i
        return len(nums)
    
# solution 3
# runtime: faster than 19.31% of submissions
# memory: less than 5.97% of submissions

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        # binary search 
        lower = 0
        upper = len(nums) - 1
        while lower <= upper:
            middle = (lower + upper)//2
            if target < nums[middle]:
                upper = middle - 1
            else:
                lower = middle + 1
        return lower
