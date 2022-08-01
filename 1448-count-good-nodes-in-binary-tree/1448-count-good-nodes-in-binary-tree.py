# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def helper(node, curr_max):
            nonlocal result
            if not node:
                return
            if node.val >= curr_max:
                result += 1
            next_max = max(curr_max, node.val)
            helper(node.left, next_max)
            helper(node.right, next_max)  
        helper(root, float('-inf'))
        return result
        
            
            
            
        