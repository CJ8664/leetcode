class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        l, r = 0, 0
        while r < len(s2):
            if s2[r] in s1_counter: 
                if s1_counter[s2[r]] > 0:
                    s1_counter[s2[r]] -= 1
                    r += 1
                else:
                    while s1_counter[s2[r]] == 0:
                        if s2[l] in s1_counter:
                            s1_counter[s2[l]] += 1
                        l += 1
            else:
                r += 1
                while l < r:
                    if s2[l] in s1_counter:
                        s1_counter[s2[l]] += 1
                    l += 1
                
            if r - l == len(s1):
                return True
        return False
            
        
        