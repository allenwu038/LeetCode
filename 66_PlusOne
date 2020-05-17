# Python3

# solution 1
# runtime: faster than 7.74% of submissions
# memory: less than 5.13% of submissions

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # turn given list of ints into one whole integer, add 1
        num = int("".join(map(str, digits))) + 1
        # return integer result as a list of separate ints
        res = list(map(int, str(num)))
        return res
        
# solution 2
# runtime: faster than 86.62% of submissions
# memory: less than 5.13% of submissions
# NOTE: though faster, it is not as readable as solution one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, str(int("".join(map(str, digits))) + 1)))
        
