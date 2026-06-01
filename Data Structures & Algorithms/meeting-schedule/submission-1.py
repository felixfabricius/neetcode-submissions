"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        # Initial solution.
        # Note that this works even if two intervals have the same start time
        # (in which case we should definitely return False).
        # Reason is that in that case there will be one case where 
        # an end time will be at an odd index. 
        # (I think... more complicated than it needs to be, though.)

        interval_times = []
        interval_dict = {}
        for interval in intervals:
            interval_times.append(interval.start)
            interval_times.append(interval.end)
            interval_dict[interval.start] = interval.end
        
        # Sort interval times
        interval_times.sort()

        # Now for each odd element in the sorted interval times, check that
            # the element is a starting time
            # and the following element is the corresponding end time
        for i in range(0, len(interval_times) - 1, 2):
            # Note that this relies on fact that if interval_times[i] is not a valid key,
            # we already return False. So then interval_dict[interval_times[i]] won't even be 
            # evaluated.
            if (
                interval_times[i] not in interval_dict 
                or interval_times[i+1] != interval_dict[interval_times[i]]
            ):
                return False
        
        return True
        """

        # New solution
        # Sort the intervals by start time
        # Then for neighbouring intervals, check that the end time of the 
        # first interval is before the start time of the next
        intervals.sort(key = lambda x: x.start)
        for i in range(0, len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        
        return True
