# Python 3
# runtime: faster than 5.02% of submissions
# memory: less than 9.53% of submissions

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[j] + nums[i] == target:
                    return [i, j]
