class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)    
        while l <= r:
            k = (l + r) // 2
            h_r = sum(math.ceil(p / k) for p in piles)
            if h_r <= h:
                r = k - 1
            else:
                l = k + 1
        return l
            
                
        