# Python3
# runtime: faster than 63.74% of submissions
# memory usage: less than 5.95% of submissions

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sortedList = []
        for i in A:
            sortedList.append(i**2)
        sortedList.sort()
        return sortedList
