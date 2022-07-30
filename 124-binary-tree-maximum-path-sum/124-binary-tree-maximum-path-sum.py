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
            # if not node.left and not node.right:
            #     return
            l_max = helper(node.left) if node.left else 0
            r_max = helper(node.right) if node.right else 0
            
            self.res = max(self.res, node.val, node.val + l_max, node.val + r_max, l_max + node.val + r_max)
            
            return max(node.val, node.val + l_max, node.val + r_max)
        
        helper(root)
        return self.res
        
            
            

        
        
        