# Python3
# runtime: faster than 94.88% of submissions
# memory: less than 5.26% of submissions

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set maxArea to 0
        # and set indexes to ends of list
        maxArea = 0
        i = 0
        j = len(height) - 1
        
        # starting from ends to the middle, compare areas
        while i < j:
            width = j - i
            length = min(height[i], height[j])
            if maxArea < width*length:
                maxArea = width*length
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
