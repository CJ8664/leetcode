# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def helper(curr, curr_sum):
            if curr_sum == targetSum and not curr.left and not curr.right:
                return True
            
            left = helper(curr.left, curr_sum + curr.left.val) if curr.left else False
            right = helper(curr.right, curr_sum + curr.right.val) if curr.right else False
            return left or right
        return helper(root, root.val)
            
        