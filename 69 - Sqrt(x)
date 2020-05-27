# Python3
# runtime: faster than 30.65% of submissions
# memory: less than 6.45% of submissions

class Solution:
    def mySqrt(self, x: int) -> int:
        lower = 0
        upper = x + 1
        while lower < upper:
            middle = (upper + lower)//2
            
            # see if middle number is the square root
            if middle*middle == x:
                return middle
            
            # if middle number too small, set lower bound to be one greater than the middle
            if middle*middle < x:
                lower = middle + 1
            
            # if middle number is too large, set middle number to be the upper bound
            else:
                upper = middle
                
        return lower - 1
