class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:       
        window = deque()
        result = []
        # Monotonic increasing queue
        for i, num in enumerate(nums):
            # The right element in queue represents the 
            # max we have seen in the window so far
            while window and window[-1][0] < num:
                window.pop()
            window.append((num, i))
            
            # Keep only k elements in window
            while i - window[0][1] + 1 > k:
                window.popleft()
            
            result.append(window[0][0])
        
        # First k - 1 elements in the result are when
        # we didn't have the full window to begin with
        return result[k - 1:]
            
        