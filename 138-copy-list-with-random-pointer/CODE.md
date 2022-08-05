```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        
        # copy nodes
        cur = head
        while cur:
            # create copy
            cur.next = Node(x=cur.val, next=cur.next)
            # move to next in original
            cur = cur.next.next
            
        # copy random pointers
        cur = head
        while cur:
            # if orig node has random ptr
            if cur.random:
                # assign the copy node with copy of random ptr
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        # separate two parts
        orig, copy = head, head.next
        result = copy
        while orig.next and copy.next:
            orig.next = orig.next.next
            orig = orig.next
            copy.next = copy.next.next
            copy = copy.next
        orig.next = None
        return result
            
        
        
                
        
        
```
