```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        q = deque()
        q.append(root)
        root.next = None
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            for i in range(len(q) - 1):
                q[i].next = q[i + 1]
            if q: q[-1].next = None
            
        return root
            
        
```
