class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        result, i = 0, 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                result += 1
                intervals[i + 1][0] = min(intervals[i][0], intervals[i + 1][0])
                intervals[i + 1][1] = min(intervals[i][1], intervals[i + 1][1])
            i += 1
        return result
                
                
        