# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left, right):
            if not node:
                return True
            # Base condition for BST
            if not (left < node.val < right):
                return False
            # All the nodes in the left tree have to be less than root
            # and also right subtree has to be great than root
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)
        return helper(root, float('-inf'), float('inf'))
            
        