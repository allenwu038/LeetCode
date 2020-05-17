# Python3
# different iterations included

# first solution
# runtime: faster than 5.85% of submissions
# memory: less than 12.31% of submissions
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        for i in range(len(haystack)):
            endStr = i + len(needle)
            if haystack[i:endStr] == needle:
                return i
        return -1
        
# second solution
# runtime: faster than 29.64% of submissions
# memory: than 13.31% of submissions
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
        
# third solution
# runtime: faster than 93.03% of submissions
# memory: less than 12.31% of submissions
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        if len(needle) > len(haystack):
            return -1
        if needle in haystack:
            return haystack.index(needle)
        return -1
