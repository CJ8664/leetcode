class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_r_pos = defaultdict(int)
        for i, c in enumerate(s):
            max_r_pos[c] = max(max_r_pos[c], i)
            
        l, r, result = 0, 0, []
        while r < len(s):
            start = l
            while l <= r:
                r = max(r, max_r_pos[s[l]])
                l += 1
            result.append(r - start + 1)
            r = l
        return result
            
            
        