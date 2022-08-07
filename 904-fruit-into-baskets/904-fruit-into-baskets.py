class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l, r = 0, 0 
        result = 1
        while r < len(fruits):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0: basket.pop(fruits[l])
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result
                
                
        
        