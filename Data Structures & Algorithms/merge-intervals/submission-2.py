class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # My initial solution:
        
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

        """
        Slightly different: explicit merge or add step after each interval.
        intervals.sort(key = lambda i : i [0])
        output = [intervals[0], intervals[1]]

        for start, end in intervals:
            if start <= output[-1][1]:
                output[-1][1] = max(intervals[-1][1], end)
            else:
                output.append([start, end])
        
        return output
        """

        """
        # Idea: sweep line algorithm. (this is basically my idea)
        # Sort intervals by start date
        # Sweep along the number line 
        # See how many intervals are active at a given moment.
        # If that number goes from 0 -> 1, then start new output interval
        # If it goes from 1 -> 0, then end the interval.

        # Interesting idea. However, I think it fails in the case where
        # one single interval has the same start and end point.
        # (which is possible based on solution constraints, but in which
        # case it wouldn't really be an 'interval').
        """

        """
        # "Greedy approach". From solutions.
        # Free recall of the algorithm here:
            # Goal: want to avoid incurring O(n log n) time cost of sorting intervals
            # Create a map which maps start times (key) to end times (value)
            # To populate this map, we need to loop through all the start and end times
            # (If there are multiple intervals with same start time, just keep track of the 
            # last end time)

            # Then loop through all the possible times at which something could be happening
            # (this is what allows us to forego the sorting). 
            # And then logic is very similar to what it used to be:
            # keep track of a results array, check if we need to merge etc.

            # Evaluation of this approach:
                # Only works well (time) if there are not too many possible start dates.
                # Or in other words: if there aren't too many potential keys 
                # (which we need to loop through in order)
            
                # This isn't more expensive in terms of space. Reason: we only store
                # the times in array which we actually need, i.e. where something actually starts.
                # (Turns out this isn't true - why??)
            # 

        # 
        """

            