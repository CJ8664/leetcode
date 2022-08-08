```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append((root, None))
        x_dep, x_par, y_dep, y_par = None, None, None, None
        depth = 0
        while q:
            for _ in range(len(q)):
                curr, par = q.popleft()
                if curr.val == x:
                    x_dep, x_par = depth, par 
                if curr.val == y:
                    y_dep, y_par = depth, par
                if curr.left: q.append((curr.left, curr.val))
                if curr.right: q.append((curr.right, curr.val))
            depth += 1
        return x_dep == y_dep and x_par != y_par
        
        
        
```
