class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if len(intervals) == 1:
            return [-1]
        
        indexes = [(float('inf'), -1)]
        for idx, interval in enumerate(intervals):
            indexes.append((interval[0], idx))
        indexes.sort()
        
        result = []
        def bin_search(num):
            l, r = 0, len(indexes) - 1
            while l <= r:
                mid = (l + r) // 2
                if indexes[mid][0] == num:
                    return indexes[mid][1]
                elif num > indexes[mid][0]:
                    l = mid + 1
                else:
                    r = mid - 1
            return indexes[l][1]
        
        for interval in intervals:
            result.append(bin_search(interval[1]))
            
        return result
                
        
            
            
            
        