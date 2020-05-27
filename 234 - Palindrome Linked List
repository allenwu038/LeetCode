# Python3
# runtime: faster than 82.71% of submissions
# memory: less than 11.54% of submissions

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # iterate through values in linked list
        # and add to a list
        res =[]
        while head != None:
            res.append(head.val)
            head=head.next
        # check that list is the same as the list reversed
        return res==res[::-1]
