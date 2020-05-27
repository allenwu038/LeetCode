# Python3
# runtime: faster than 81.66% of submissions
# memory: less than 5.69% of submissions

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        # one option if nums has only one element
        if len(nums) == 1:
            return nums[0]
            
        # maxSum will be the largest sum encountered
        maxSum = nums[0]
        
        # currSum is a cumulative sum that is reset when the curret element is larger than previous elements summed
        currSum = nums[0]
        
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(currSum, maxSum)
        return maxSum
