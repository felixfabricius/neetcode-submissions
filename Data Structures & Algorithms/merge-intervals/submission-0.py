class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged_intervals = []

        # Is there a way to avoid this?
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] <= curr_end:
                if interval[1] > curr_end:
                    curr_end = interval[1]
            else:
                merged_intervals.append([curr_start, curr_end])
                curr_start = interval[0]
                curr_end = interval[1]

        merged_intervals.append([curr_start, curr_end])
        
        return merged_intervals
            