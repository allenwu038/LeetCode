# Python3
# runtime: faster than 72.35% of submissions
# memory: less than 5.97% of submissions
# NOTE: this question is very similar to questions about tiling a 1xn board
# with squares and dominos 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # we can use the closed form of the Fibonacci numbers
        return int((1/sqrt(5))*(((1+sqrt(5))/2)**(n+1) -((1-sqrt(5))/2)**(n+1)))
