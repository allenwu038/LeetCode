# Python3
# runtime: faster than 63.74% of submissions
# memory usage: less than 5.95% of submissions

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sortedList = []
        # square elements in A and put in new list
        for i in A:
            sortedList.append(i**2)
        # sort the squared elements and return the new sorted list
        sortedList.sort()
        return sortedList
