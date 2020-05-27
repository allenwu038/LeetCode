# Python3

# solution 1
# runtime: faster than 10.49% of submissions
# memory: less than 8.70% of submissions

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        # keep track of the maxLength
        maxLength = 1
        count = 1
        # iterate over elements in nums, and reset count when next element less than current element
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                count +=1
            else:
                count = 1
            if count > maxLength:
                maxLength = count
        return maxLength

# solution 2
# runtime: faster than 15.44% of submissions
# memory: less than 8.70% of submissions

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        maxLength = 1
        count = 1
        previous = nums[0]
        for current in nums:
            # compare current number in nums to the one before
            if previous < current:
                count +=1
            else:
                count = 1
            if count > maxLength:
                maxLength = count
            previous = current
        return maxLength
