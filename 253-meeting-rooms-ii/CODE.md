```python
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start_times = sorted(interval.start for interval in intervals)
        end_times = sorted(interval.end for interval in intervals)

        s_idx, e_idx, result, active_meetings = 0, 0, 0, 0
        while s_idx < len(start_times):
            # Meeting started before the current end
            if start_times[s_idx] < end_times[e_idx]:
                active_meetings += 1
                s_idx += 1
            # Meeting starts at the current end or after
            else:
                active_meetings -= 1
                e_idx += 1
            result = max(result, active_meetings)
        return result 
```