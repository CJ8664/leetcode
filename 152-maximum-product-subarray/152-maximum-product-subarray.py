class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Assume the min and max product before the array is 1
        # Also, the max sub array could indeed be the max element in array
        max_prefix, min_prefix, result = 1, 1, max(nums)
        
        for n in nums:
            # This is equivalent to saying that we cannot make
            # previously visited part of array a part of result 
            # sub-array in other words we restart our search 
            if n == 0:
                max_prefix, min_prefix = 1, 1
                continue
            # The max and min obtained by multiplying curr num
            t_max, t_min = max_prefix * n, min_prefix * n
            # If the min prefix was negative and n is also negative, the 
            # product is now postive, hence it is considered while getting
            # the max prefix uptil this point. Also, if n itself is greater 
            # than t_min and t_max, forget all the previously visited elements
            # and start considering the result (sub array) from n.
            # Similar explanation for max prefix
            max_prefix, min_prefix = max(t_max, t_min, n), min(t_max, t_min, n)
            result = max(result, max_prefix)
        return result
        