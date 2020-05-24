# Python3
# runtime: faster than 97.94% of submissions
# memory: less than 6.15% of submissions

class Solution:
    def intToRoman(self, num: int) -> str:
    
        # dictionary for ints and corresponding roman letter
        translation = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        
        # the result begins as an empty string
        res = ""

        # iterate through number and roman letter key/value pairs in dictionary
        for number, roman in translation.items():
        
            # we can floor divide given num by number key in dictionary
            # and add the correspinding roman letter to res
            res += roman * (num//number)
            
            # now we must mod num by number so we iterate through digits of num
            num %= number
            
        return res
