"""
Approach:
# Number of elements we need to keep track of as a function of how many elements we've added so far:
# 1: 1
# 2: 2
# 3: 2
# 4: 3
# 5: 3
# 6: 4
# 7: 4
# Need to keep track of the largest (n + 2) // 2 = n // 2 + 1 items
# Among those items, interested either in the smallest 1 (if n is odd) or in the smallest
# 2 items.
# This can be solved using heap.

# Issue: as we go from odd to even, 
    # there can be the case that we now need to keep track of a number we previously ignored,
    # which might be the lower half of the median

# Updated to account for this:
# 1: 1
# 2: 2
# 3: 3
# 4: 3
# 5: 4
# 6: 4
# 7: 5

# From 2 onwards: 
    # (n + 1) // 2 + 1

# But since we're just using this to pop, can always use this as condition.

# Now: 
# Becomes less obvious how to find the median for the odd elements!


"""


class MedianFinder:

    def __init__(self):
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, num)
        self.n += 1
        while len(self.min_heap) > (self.n + 3) // 2:
            heapq.heappop(self.min_heap)

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            if self.n == 1:
                return self.min_heap[0]
            return min(self.min_heap[1], self.min_heap[2])
        else:
            if self.n == 2:
                return (self.min_heap[0] + self.min_heap[1]) / 2
            else:
                print(min(self.min_heap[1], self.min_heap[2]))
                return (self.min_heap[0] + min(self.min_heap[1], self.min_heap[2])) / 2
            
        
        