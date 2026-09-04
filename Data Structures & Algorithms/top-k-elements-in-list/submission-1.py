class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approaches:
        """
            1. Count occurences for each element (O(n))
            2. Collect the items 
            3. Sort items by the count and return the items (O(n log n))
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_counts[:k]]

            # 
            # Collect the items
            # Sort the items by the count, and return the items
