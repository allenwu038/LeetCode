# Python 3
# runtime: faster than 70.63% of submissions
# memory: less than 6.90% of submissions

# The isBadVersion API is already defined for you.

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lowerBound = 1
        upperBound = n
        while lowerBound < upperBound:
            // find the middle of the eligible values
            middle = lowerBound + (upperBound-lowerBound)//2
            // if middle is already a bad version, the first must come before it
            if isBadVersion(middle):
                upperBound = middle
            else:
                # if middle is not a bad version, the first must come after it
                lowerBound = middle + 1
        return lowerBound
