class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        result = 0
        for idx in range(len(intervals) - 1):
            left, right = intervals[idx], intervals[idx + 1]
            # The left meeting ends after the start of right ( overlaps )
            if left[1] > right[0]:
                result += 1
                intervals[idx + 1][0] = min(left[0], right[0])
                # drop the meeting that is longer as it may 
                # overlap with other too
                intervals[idx + 1][1] = min(left[1], right[1])
        return result
        