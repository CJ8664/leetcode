class Solution:
    def trap(self, height: List[int]) -> int:
        # For a given index find the largest wall
        # on the left side and right side
        left_max = [0 for _ in range(len(height))] 
        right_max = [0 for _ in range(len(height))]
        
        l, r = 1, len(height) - 2
        for _ in range(1, len(height) - 1):
            left_max[l] = max(left_max[l - 1], height[l - 1])
            right_max[r] = max(right_max[r + 1], height[r + 1])
            l += 1
            r -= 1
        
        # At any given index the area of water it determeined the min 
        # height of the left and right wall. Also, since the index can
        # have its height we have to subtract that from the min of 
        # left and right wall
        res = 0
        for i in range(len(height)):
            max_h = min(left_max[i], right_max[i])
            if height[i] < max_h:
                res += (max_h - height[i])
        return res
            
            
        