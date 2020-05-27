# Python3
# runtime: faster than 93.81% of submissions
# memory: less than 7.69% of submissions

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        # if there is no root, return true because all the values are null
        if not root:
            return True
        
        # if the root is not null, save it as the univalue
        else:
            uniVal = root.val
            
            # recursive helper function to check that all other nodes have the same univalue
            def traverseAndCheck(root):
                if root == None:
                    return True
                return (root.val == uniVal) and traverseAndCheck(root.left) and traverseAndCheck(root.right)
                
            # have helper take root in as argument and return boolean
            return traverseAndCheck(root)
