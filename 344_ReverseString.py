# Python3
# runtime: faster than 81.96% of submissions
# memory: less than 5.81% of submissions

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # loop to switch elements mirrored around middle of list 
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]
        
