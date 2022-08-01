```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = collections.deque()
        curr = root
        
        while stack or curr:
            # traverse all the way to the leftmost child
            while curr:
                stack.append(curr)
                curr = curr.left
            # process leftmost node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            # visit right node of "V"
            curr = curr.right
```
