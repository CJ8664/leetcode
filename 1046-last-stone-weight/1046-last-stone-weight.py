class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        # This is required so that we can use Max heap
        for idx in range(len(stones)):
            stones[idx] *= -1
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones, first - second)
        return heapq.heappop(stones) * -1 if len(stones) > 0 else 0
                
            
            
        