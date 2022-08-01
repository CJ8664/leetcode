```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the mid of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        prev, curr = None, slow
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        
        # Splice together nodes
        list1, list2 = head, prev
        dummy = ListNode()
        curr = dummy
        toggle = 1
        while list1 and list2:
            if toggle == 1:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            toggle *= -1
        return dummy.next
                
            
            
        
        
```
