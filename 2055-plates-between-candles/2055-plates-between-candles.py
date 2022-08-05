class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        l, r = 0, len(s) - 1
        nearest_right_candle = [-1 for _ in range(len(s))]
        nearest_left_candle = [-1 for _ in range(len(s))]
        candle_count = [0 for _ in range(len(s))]
        
        for _ in range(len(s)):
            nearest_left_candle[l] = l if s[l] == "|" else (nearest_left_candle[l - 1] if l > 0 else -1)
            nearest_right_candle[r] = r if s[r] == "|" else (nearest_right_candle[r + 1] if r < len(s) - 1 else -1)
            candle_count[l] = candle_count[l-1] + 1 if s[l] == "|" else candle_count[l-1]
            l, r = l + 1, r - 1
                
        result = []
        for l, r in queries:
            nrc, nlc = nearest_right_candle[l], nearest_left_candle[r]
            if nrc == -1 or nlc == -1:
                result.append(0)
            elif nlc - nrc > 0:
                cl, cr = candle_count[nrc], candle_count[nlc]
                result.append((nlc - nrc + 1) - (cr - cl + 1))
            else:
                result.append(0)
        
        return result
            
        