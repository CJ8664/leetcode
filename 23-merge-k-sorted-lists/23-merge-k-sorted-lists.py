# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        # heapq.heapify(h)
        # result = ListNode()
        # curr = result
        # while len(h) > 0:
        #     _, idx = heapq.heappop(h)
        #     curr.next = lists[idx]
        #     if lists[idx].next:
        #         lists[idx] = lists[idx].next
        #         heapq.heappush(h, (lists[idx].val, idx))
        #     curr = curr.next
        # return result.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next



            
            
        
        