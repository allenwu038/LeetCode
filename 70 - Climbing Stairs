# Python3
# NOTE: this question is very similar to questions about tiling a 1xn board
# with squares and dominos 

# solution 1
# runtime: faster than 91.48% of submissions
# memory: less than 5.97% of submissions
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        # we can use the closed form of the Fibonacci numbers
        return int((1/sqrt(5))*(((1+sqrt(5))/2)**(n+1) -((1-sqrt(5))/2)**(n+1)))

# solution 2
# runtime: faster than 72.35% of submissions
# memory: less than 5.97% of submissions
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        # this does not use the closed form of Fibonacci numbers
        # and instead uses the recursive sequence
        seq = [None] * (n+1)
        seq[0] = 1
        seq[1] = 1
        for i in range(2,n+1):
            seq[i] = seq[i-1] + seq[i-2]
        return seq[n]
