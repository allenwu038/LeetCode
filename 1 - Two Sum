# Python 3
# runtime: faster than 5.02% of submissions
# memory: less than 9.53% of submissions

# note: could run faster if hash maps were used 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate over elements of nums
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                # when we find a pair of elements that add to the target value, return them
                if i != j and nums[j] + nums[i] == target:
                    return [i, j]
