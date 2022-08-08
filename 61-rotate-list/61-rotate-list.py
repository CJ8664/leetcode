# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Get the length
        curr, l, tail = head, 0, None
        while curr:
            if curr.next == None: tail = curr
            curr, l = curr.next, l + 1
                
        # Number of nodes in first part
        stop_idx = l - (k % l)
        
        # If the entire list is the first part
        if stop_idx == l:
            return head
        
        # Get to the end of result list
        curr = head
        for _ in range(stop_idx - 1):
            curr = curr.next
            
        result = curr.next
        curr.next = None
        tail.next = head
        return result
        
        