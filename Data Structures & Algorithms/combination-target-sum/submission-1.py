class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(subset, target): 
            for num in nums:
                if (
                    subset and subset[-1] > num
                    or num > target
                ):
                    continue
                if num == target:
                    res.append(subset + [num]) # no need to further pursue this path
                dfs(subset + [num], target - num)
        
        dfs([], target)
        
        return res