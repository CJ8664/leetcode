class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the rightmost idx where a particular element 
        # can be found in the string
        max_r_pos = {c:i for i, c in enumerate(s)}
        # Left indicates the begining of the substring, Right
        # indicates the current max right of substring
        l, r, idx = 0, 0, 0
        result = []
        while idx < len(s):
            r = max(r, max_r_pos[s[idx]])
            if idx == r:
                result.append(r - l + 1)
                l = r + 1
            idx += 1
        return result
                
        