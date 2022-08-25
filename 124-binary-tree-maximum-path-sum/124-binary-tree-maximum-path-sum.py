# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def helper(node):
            nonlocal res
            # IF does not have left its left subtree value is 0
            l_max = helper(node.left) if node.left else 0
            # IF does not have right its left subtree value is 0
            r_max = helper(node.right) if node.right else 0
            
            # max val at current node can be the node itself if
            # the children bring negative value
            curr_max = max(node.val, node.val + l_max, node.val + r_max)
            
            # Result can be multiple combination
            res = max(res, curr_max, l_max + node.val + r_max)
            
            return curr_max
        
        helper(root)
        return res
        
            
            

        
        
        