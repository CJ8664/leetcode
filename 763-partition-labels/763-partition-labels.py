class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        max_pos = {}
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] not in max_pos:
                max_pos[s[idx]] = idx
        l, r, idx = 0, 0, 0
        result = []
        while idx < len(s):
            r = max(r, max_pos[s[idx]])
            if idx == r:
                result.append(r - l + 1)
                l = r + 1
            idx += 1
        return result
                
        