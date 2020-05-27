# Python3
# runtime: faster than 86.53% of submissions
# memory: less than 5.41% of submissions

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # we can add a and b as ints first, and then figure out the math in binary
        numSum = int(a)+int(b)
        numStr = list(str(numSum))
        
        # we need to add a zero at the very front for a carry
        numStr.insert(0, '0')
        
        # iterate through the sum as a string from the back to the front
        for i in range(len(numStr))[::-1]:
        
            # implement rules for carry
            if numStr[i]=="2":
                numStr[i-1]=str(int(numStr[i-1])+1)
                numStr[i]="0"
            if numStr[i]=="3":
                numStr[i-1]=str(int(numStr[i-1])+1)
                numStr[i]="1"
        
        # return result in string form
        res = int("".join(numStr))
        return str(res)
