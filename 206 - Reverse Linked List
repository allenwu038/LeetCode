# Python3
# runtime: faster than 64.80% of submissions
# memory: less than 27.27% of submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# NOTE: we will change the linked list in place by pointing every node.next to the previous node

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # use three pointers to keep track
        previous = None
        current = head
        following = head
        
        # while the current pointer is not at the end of the linked list, iterate
        while current != None:
        
            # save where current points to by moving the following pointer
            following = following.next
            
            # reverse the order in which the current node points
            current.next = previous
            
            # iterate one element over
            previous = current
            current = following
            
        # previous will be the head of the newly reversed linked list
        return previous
