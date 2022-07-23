class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_r_pos = defaultdict(int)
        for i, c in enumerate(s):
            max_r_pos[c] = max(max_r_pos[c], i)
            
        l, r, i = 0, 0, 0
        result =[]
        while r < len(s):
            l = i
            while i <= r:
                if max_r_pos[s[i]] > r: r = max_r_pos[s[i]]
                i += 1
            result.append(r - l + 1)
            r = i
        return result
            
            
        