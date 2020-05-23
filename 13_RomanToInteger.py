# Python3
# runtime: faster than 99.20% of submissions
# memory: less than 5.38% of submissions

class Solution:
    def romanToInt(self, s: str) -> int:
    
        # dictionary to store int values of the roman numerals
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        # set our result to zero, and initiate a prev variable since we know roman numerals
        # are typically written largest to smallest and the cases we need to subtract in are the
        # ones where the previous char is less than the current
        
        res = 0
        prev = 1001
        
        for char in s:
            if dict[char] <= prev:
                res += dict[char]
            else:
                res += dict[char] - 2*prev
            prev = dict[char]
        return res

