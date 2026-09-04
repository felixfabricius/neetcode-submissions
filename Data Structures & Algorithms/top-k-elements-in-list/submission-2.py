import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Approaches:
        """
        1) Keep track of counts in hashtable, then sort
            1. Count occurences for each element (O(n))
            2. Collect the items 
            3. Sort items by the count and return the items (O(n log n))

            counts = {}
            for num in nums:
                counts[num] = counts.get(num, 0) + 1
            sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            return [item[0] for item in sorted_counts[:k]]

        2) Count everything; then heapify by those counts, and pop from heap k times.
        Question: how can I "heapify the dictionary"? Can heapify counts.
        Note that we can heapify tuples!!! And then the first item determines priorities.
        (And subsequent items only matter when ties.)
        Could build a custom heap structure...
        """
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        heap = [(count, val) for val, count in counts.items()]
        heapq.heapify_max(heap)
        
        output = []
        for i in range(k):
            output.append(heapq.heappop_max(heap)[1])

        return output
        
        
        