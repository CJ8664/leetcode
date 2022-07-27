# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        if not root:
            return 0
        stack = deque()
        stack.append((root, 1))
        result = 1
        while stack:
            node, h = stack.pop()
            result = max(result, h)
            if node.right: stack.append((node.right, h + 1))
            if node.left: stack.append((node.left, h + 1))
        return result            
            