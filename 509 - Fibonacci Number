# Python3
# runtime: faster than 99.82% of submissions
# memory: less than 5.80% of submissions

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        # populate a list using the recursive form of Fibonnaci numbers
        seq = [None]*(N+1)
        seq[0] = 0
        seq[1] = 1
        for i in range(2, N+1):
            seq[i] = seq[i-1] + seq[i-2]
        return seq[N]
