```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l, r = 0, 0 
        result = 1
        while r < len(fruits):
            # Add current fruit to basket
            basket[fruits[r]] += 1
            # If the number of distinct fruits in basket are greater 
            # than 2 than remove the fruits from the left of the window
            # till only 2 types of fruits remain in basket
            while len(basket) > 2:
                basket[fruits[l]] -= 1
                # if the count of this fruit type is 0, remove it from
                # basket
                if basket[fruits[l]] == 0: basket.pop(fruits[l])
                l += 1
            result = max(result, r - l + 1)
            r += 1
        return result
                
                
        
        
```
