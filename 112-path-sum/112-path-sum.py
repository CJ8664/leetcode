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
        
        #####################
        ##### RECURSIVE #####
        #####################
        
        def helper(curr, curr_sum):
            if curr_sum == targetSum and not curr.left and not curr.right:
                return True
            
            left = helper(curr.left, curr_sum + curr.left.val) if curr.left else False
            right = helper(curr.right, curr_sum + curr.right.val) if curr.right else False
            return left or right
        return helper(root, root.val)
    
        #####################
        ##### ITERATIVE #####
        #####################
            
        stack = [(root, root.val)]
        while stack:
            cur, pathsum = stack.pop()
            if not cur.left and not cur.right and pathsum == targetSum:
                return True
            if cur.left:
                stack.append((cur.left, pathsum + cur.left.val))
            if cur.right:
                stack.append((cur.right, pathsum + cur.right.val))
        return False
        