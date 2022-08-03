```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko can eat minimum of 1 banan OR max(piles) in one seating
        l, r = 1, max(piles)     
        while l <= r:
            # Mid way between the min and max banana Koko can eat in one 
            # seating
            k = (l + r) // 2
            # Num of hours req by Koko to eat all piles at rate k
            h_r = sum(math.ceil(p / k) for p in piles)
            # If Koko is eating fast, decrease the max banana koko
            # should eat
            if h_r <= h:
                r = k - 1
            # not eating fast enough, increase the min banana koko 
            # should eat
            else:
                l = k + 1
        # The result is the min banana
        return l
            
                
        
```
