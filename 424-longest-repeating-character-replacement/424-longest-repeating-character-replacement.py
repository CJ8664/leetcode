class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        l, r = 0, 0
        curr_size, result = 0, 0
        while r < len(s):
            char_freq[s[r]] += 1
            curr_size += 1
            # Cannot make substitution
            while curr_size - max(char_freq.values()) > k:
                char_freq[s[l]] -= 1
                curr_size -= 1
                l += 1
            else:
                result = max(result, curr_size)
            r += 1
        return result
                
                
                
            
            
        
        
                
                
            
            
        