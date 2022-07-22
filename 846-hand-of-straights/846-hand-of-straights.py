class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False
        result = []
        for _ in range(len(hand) // groupSize):
            result.append([])
        hand.sort()
        for h in hand:
            placed = False
            for r in result:
                if len(r) == groupSize:
                    continue
                if not r or h == r[-1] + 1:
                    r.append(h)
                    placed = True
                    break
            if not placed:
                return False
        return True
                
                
            
        