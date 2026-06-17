"""
Subproblems: maximum amount of money you can obtain breaking into nums[:i], i = 1, ..., n; f(i)
Relation between the problembs: f(i) = max(f(i - 2) + nums[i - 1], f(i - 1))

Why does this work?

Time complexity of this approach:
- O(n)
- Space complexity: O(1)
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        neg_2 = 0
        neg_1 = 0

        for i in range(len(nums)):
            neg_2, neg_1 = neg_1, max(neg_2 + nums[i], neg_1)

        return neg_1
