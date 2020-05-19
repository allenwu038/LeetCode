# Python3
# runtime: faster than 42.83% of submissions
# memory: less than 6.50% of submissions

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # cast x as a string
        stringX = str(x)
        length = len(stringX)
        count = 0
        
        # check that the first half of the string matches 
        # reverse of the second half of the string 
        for i in range(length//2):
            if stringX[i] == stringX[length-i-1]:
                count += 0
            else:
                count +=1
        return (count==0)
