class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [-1, -1, -1]
        tx, ty, tz = target
        for x, y, z in triplets:
            # Fill the buckets till you have space If there 
            # is no space left in any of the buckets then stop
            if x <= tx and y <= ty and  z <= tz:
                res[0] = max(res[0], x)
                res[1] = max(res[1], y)
                res[2] = max(res[2], z)
        # Check if all the buckets are filled
        return all([a==x for a, x in zip(target, res)])
            
            
        