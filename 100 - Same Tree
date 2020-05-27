# Python3
# runtime: faster than 97.67% of submissions
# memory: less than 5.72% of submissions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if both trees are empty they are equal
        if p == None and q == None:
            return True
        # if only one of the trees is empty they cannot be equal
        if (not q or not p):
            return False
        # if the values at nodes aren't equal, the trees aren't equal
        if p.val != q.val:
            return False
        # recurse to the bottom of the tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
