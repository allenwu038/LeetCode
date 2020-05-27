# Python3
# runtime: faster than 57.31% of submissions
# memory: less than 8.70% of submissions

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # base cases include if nums is empty or if 1 is not in nums
        if nums == []:
            return 1
        elif 1 not in nums:
            return 1
            
        #largestPostive is the largest the missing positive can be
        else:
            largestPositive = max(nums)
            for i in range(1, largestPositive + 1):
                if i not in nums:
                    return i
            return largestPositive+1
          
