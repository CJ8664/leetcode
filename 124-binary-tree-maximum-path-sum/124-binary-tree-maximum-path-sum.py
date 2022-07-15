# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float('-inf')
        def helper(node):
            if not node:
                return 0
            l_max = helper(node.left)
            r_max = helper(node.right)
            self.max_path = max(self.max_path, node.val + l_max + r_max, node.val + l_max, node.val + r_max, node.val) 
            return max(l_max + node.val, r_max + node.val, node.val)
        helper(root)
        return self.max_path
        
        