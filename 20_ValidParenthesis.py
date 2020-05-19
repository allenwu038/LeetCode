# Python3
# runtime: faster than 73.13% of submissions
# memory: less than 5.22% of submissions

class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty stack
        stack = []
        
        # create a dictionary with matching paretheses as keys and values
        d = {')': '(', '}': '{', ']' : '['}
        
        # iterate over each character in s
        for c in s:
        
            # if c is one of the values in d (or an open parethesis)
            #add it to the stack
            if c in d.values():
              stack.append(c)
            
            # if c is a key (closing parenthesis), then the 
            # corresponding value (open parenthesis) should be on the stack
            elif not stack or stack.pop() != d[c]:
              return False
              
        # if a valid string was passed, stack should be empty
        return True if not stack else False
    
