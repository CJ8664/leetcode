class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))] 
        right_max = [0 for _ in range(len(height))]
        
        l, r = 1, len(height) - 2
        for _ in range(1, len(height) - 1):
            left_max[l] = max(left_max[l - 1], height[l - 1])
            right_max[r] = max(right_max[r + 1], height[r + 1])
            l += 1
            r -= 1
        res = 0
        for i in range(len(height)):
            max_h = min(left_max[i], right_max[i])
            if height[i] < max_h:
                res += (max_h - height[i])
        return res
            
            
        