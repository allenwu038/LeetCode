# Python3
# runtime: faster than 70.54% of submissions
# memory: less than 5.26% of submissions

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # get rid of whitespaces, and check if empty
        # this means strings like "" or "    " return 0
        if not s.strip():
            return 0
         
        # make a list of all the words in s, split by spaces
        words = s.split()
        n = len(words)
        
        # return the length of word in list at last index
        return len(words[n-1])
