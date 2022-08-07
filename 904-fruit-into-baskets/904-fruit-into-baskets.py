class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        current_basket = defaultdict(int)
        l, r = 0, 0 
        result = 1
        while r < len(fruits):
            if len(current_basket) < 2 or fruits[r] in current_basket:
                current_basket[fruits[r]] += 1
                result = max(result, r - l + 1)
                r += 1
            else:
                # print(l, r, current_basket)
                while len(current_basket) >= 2:
                    current_basket[fruits[l]] -= 1
                    if current_basket[fruits[l]] == 0:
                        del current_basket[fruits[l]]
                    l += 1
        return result
                
                
        
        