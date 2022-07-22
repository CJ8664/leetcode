class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        
        n_g = len(hand) // groupSize
        result = []
        for _ in range(n_g):
            result.append([])

        heapq.heapify(hand)
        while hand:
            h = heapq.heappop(hand)
            placed = False
            for r in result:
                if (len(r) < groupSize) and (len(r) == 0 or r[-1] == h - 1):
                    r.append(h)
                    placed = True
                    break
            if not placed:
                return False
        return True
        
                
                
            
        