class Solution:
    def numDecodings(self, s: str) -> int:
        memory = {len(s): 1}
        def helper(idx):
            if idx in memory:
                return memory[idx]
            if s[idx] == "0":
                return 0
            res = helper(idx + 1)
            #  (s[idx] == "1" or (s[idx] == "2" and s[idx + 1] in "0123456"))
            if idx + 1 < len(s) and int(s[idx:idx + 2]) <= 26:
                res += helper(idx + 2)
            memory[idx] = res
            return res
        return helper(0)
                

        