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
        while n > 0:
            offset = offset.next
            n -= 1
        
        # Reach the node who's next we want to delete
        start = dummy
        while offset.next:
            start = start.next
            offset = offset.next
        
        # Delete the node
        start.next = start.next.next
        
        return dummy.next
            
            
        