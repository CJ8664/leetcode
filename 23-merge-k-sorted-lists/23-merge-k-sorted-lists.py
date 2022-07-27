# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, nxt):
        return self.val < next.val
    
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        result = ListNode()
        curr = result
        while len(h) > 0:
            _, idx = heapq.heappop(h)
            curr.next = lists[idx]
            if lists[idx].next:
                lists[idx] = lists[idx].next
                heapq.heappush(h, (lists[idx].val, idx))
            curr = curr.next
        return result.next
            
            
        
        