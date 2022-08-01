```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def helper(node):
            nonlocal result
            l_h = helper(node.left) if node.left else 0
            r_h =  helper(node.right) if node.right else 0
            result = max(result, l_h + r_h)
            return 1 + max(l_h, r_h) 
        helper(root)
        return result
        
```
