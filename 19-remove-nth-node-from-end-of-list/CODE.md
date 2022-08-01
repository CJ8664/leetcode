```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        offset = dummy
        # Give a head start to make offset
        for _ in range(n):
            offset = offset.next
        
        # Reach the node who's next we want to delete
        start = dummy
        while offset.next:
            start = start.next
            offset = offset.next
        
        # Delete the node
        start.next = start.next.next
        
        return dummy.next
            
            
        
```
