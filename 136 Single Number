# Python3
# runtime: faster than 21.53% of submissions
# memory: less than 6.56% of submissions

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #sort the list of ints
        nums.sort()
        
        #iterate over ints in list in pairs
        for i in range(0, len(nums) - 1, 2):
            #if a pair does not match, the first number must be single
            if nums[i] != nums[i+1]:
                return nums[i]
                
        #otherwise, the last number must be the single
        return nums[len(nums) - 1]
