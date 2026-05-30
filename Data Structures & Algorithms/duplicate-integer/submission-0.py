class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        # O(n^2) solution
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        """
        # O(n) solution
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
