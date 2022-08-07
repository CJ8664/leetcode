class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        if s1_counter == s2_counter:
            return True
        l, r = 0, len(s1)
        while r < len(s2):
            s2_counter[s2[r]] += 1
            s2_counter[s2[l]] -= 1
            if s2_counter[s2[l]] == 0:
                s2_counter.pop(s2[l])
            if s1_counter == s2_counter:
                return True
            l, r = l + 1, r + 1
        return False
            
            
        
        