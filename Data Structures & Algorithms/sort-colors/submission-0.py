class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use bucket sort.
        counts = [0, 0, 0]

        for val in nums: 
            counts[val] += 1
        
        j = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[j] = i
                j += 1
        