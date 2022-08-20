class Solution:
    def uniqueLetterString(self, s: str) -> int:
        windows = defaultdict(list)
        for idx, c in enumerate(s):
            windows[c].append(idx)
            
        result = 0
        for c in windows:
            pos = [-1] + windows[c] + [len(s)]
            i = 1
            while i < len(pos) - 1:
                result += (pos[i] - pos[i - 1]) * (pos[i + 1] - pos[i])
                i += 1
        return result
                    
                
                
            
               
        
            