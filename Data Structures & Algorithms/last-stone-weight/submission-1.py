"""
Implementation approaches:
1. Sort list of stones at beginning, and then at each iteration.
    - Sorting at beginning: O(n log n)
    - Sorting at each iteration totals O(n^2)
2. Use heap:
    - heapq.heapify_max() is O(n)
    - work at each iteration: O(log n)
    -> total work: O(n log n), with O(1) space (check if heap is O(1) space or O(n) space)
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if x != y:
                heapq.heappush_max(stones, max(x, y) - min(x, y))
        
        if stones:
            return stones[0]
        return 0