class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        l, r = 0, 0
        
        while r < len(s2):
            # Move r pointer forward till we find first occurrance 
            # of any char in s1
            if s2[r] not in s1_counter:
                r += 1
                continue
            # We want to start tracking s1 from r so we
            # have to bring l at same position as r
            while l < r:
                if s2[l] in s1_counter:
                    s1_counter[s2[l]] += 1
                l += 1
            
            # Window logic
            while r < len(s2) and s2[r] in s1_counter:
                # If the char at r is already used up 
                # shrink window from left until we restore that char
                while s1_counter[s2[r]] == 0:
                    if s2[l] in s1_counter:
                        s1_counter[s2[l]] += 1
                    l += 1
                # IF char at r is in s1 decrement its counter
                s1_counter[s2[r]] -= 1
                r += 1
                
                # IF the window size is len of s1 return true
                if r - l == len(s1):
                    return True
        return False
            
        
        