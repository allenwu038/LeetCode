# Python3
# runtime: faster than 83.67% of submissions
# memory: less than 5.26% of submissions

class Solution:
    def reverse(self, x: int) -> int:
    
        # for a negative number, make sure negative sign is still in front
        # use string manipulation to reverse numbers 
        if x<0:
            solution = -int(str(x)[1:][::-1])
        else:
            solution = int(str(x)[::-1])
            
        if -2**31 <= solution <= 2**31-1:
            return solution
            
        # return zero if the reversed integer overflows
        else:
            return 0
        
