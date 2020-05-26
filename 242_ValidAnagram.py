# Python3

# solution 1
# runtime: faster than 5.33% of submissions
# memory: less than 6.25% of submissions

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            letters = list(t)
            for char in s:
                if char in letters:
                    letters.remove(char)
        return letters == []
        
# solution 2
# runtime: faster than 99.79% of submissions
# memory: less than 9.38% of submissions

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # make use of Python counter tool in collections class
        return Counter(s) == Counter(t)

