class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value_counts = {}

        for num in nums:
            value_counts[num] = value_counts.get(num, 0) + 1
        
        return [
            num for num, count 
            in sorted(
                value_counts.items(), 
                key=lambda x : x[1], 
                reverse=True
            )[:k]
        ]