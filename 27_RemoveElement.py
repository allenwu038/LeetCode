# Python3
# runtime: faster than 88.95% of submissions
# memory: less than 6.06% of submissions

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            # remove all instances of val from nums
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
                
