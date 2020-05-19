# Python3

# solution 1
# runtime: faster than 6.71% of submissions
# memory: less than 6.70% of submissions

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        # use fraction if n is negative
        if n < 0:
            x = 1/x
            n = abs(n)
        res = 1
        while (n > 0):
            if n%2 == 1:
                res = res * x
                n = n - 1
            else:
                x = x*x
                n = n//2
        return res
        
# solution 2
# runtime: faster than 91.88% of submissions
# memory: less than 6.90% of submissions

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = abs(n)
        res = 1
        while (temp > 0):
            if temp%2 == 1:
                res = res * x
                temp -=  1
            else:
                x *= x
                temp //= 2
        # deal with negative power at the very end
        return res if n > 0 else 1/res
