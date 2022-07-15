# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = collections.deque()
        stack.append((root, float('-inf')))
        result = []
        while stack:
            curr_node, curr_max = stack.pop()
            if curr_node.val >= curr_max:
                result.append(curr_node.val)
            next_max = max(curr_max, curr_node.val)
            if curr_node.right:
                stack.append((curr_node.right, next_max))
            if curr_node.left:
                stack.append((curr_node.left, next_max))
        return len(result)
            
            
        
        