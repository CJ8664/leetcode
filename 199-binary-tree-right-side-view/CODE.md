```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if not root: return result
        q = deque()
        q.append(root)
        while q:
            # Level order traversal
            level_len = len(q)
            for i in range(level_len):
                node = q.popleft()
                # Last element in the current level
                if i == level_len - 1:
                    result.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return result
        
        
        
```
