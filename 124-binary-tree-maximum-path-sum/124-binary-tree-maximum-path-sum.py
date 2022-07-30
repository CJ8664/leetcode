# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def helper(node):
            # nonlocal res
            
            if not node: return 0

            l_max = helper(node.left)
            r_max = helper(node.right)
            
            self.res = max(self.res, node.val, node.val + l_max, node.val + r_max, l_max + node.val + r_max)
            
            return max(node.val, node.val + l_max, node.val + r_max)
        
        helper(root)
        return self.res
        
            
            

        
        
        