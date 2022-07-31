# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def helper(node):
            l_h, l_b = helper(node.left) if node.left else (0, True)
            r_h, r_b = helper(node.right) if node.right else (0, True)
            return (1 + max(l_h, r_h), l_b and r_b and abs(l_h - r_h) <= 1)
        _, result = helper(root)
        return result
            
        