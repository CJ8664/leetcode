class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [copy.copy(nums)]
        result = []
        
        for i in range(len(nums)):
            n = nums.pop(0)
            # print(f"aux {nums}")
            perms = self.permute(nums)
            for p in perms:
                p.append(n)
            result.extend(perms)
            # print(f"res: {result}")
            nums.append(n)
        return result
        