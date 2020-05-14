# Python3
# runtime: faster than 63.74%
# memory usage: less than 5.95%

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sortedList = []
        for i in A:
            sortedList.append(i**2)
        sortedList.sort()
        return sortedList