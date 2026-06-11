# Trivial solution: sorting. O(n log n)
# Better: max heap. This has complexity:
    # O(n) + k * O(log n)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        for _ in range(k - 1):
            heapq.heappop_max(nums)
        return nums[0]