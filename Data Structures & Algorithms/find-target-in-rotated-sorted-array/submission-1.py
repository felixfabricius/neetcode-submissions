class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            m = l + (h - l) // 2 # left middle element
            if nums[l] == target:
                return l
            if nums[m] == target:
                return m
            if (
                (nums[l] < nums[m] 
                and nums[l] < target < nums[m])
                or (nums[l] > nums[m]
                and not nums[m] < target < nums[l])
            ):
                l += 1
                h = m - 1
            else:
                l = m + 1
        
        return -1
