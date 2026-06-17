"""
Approach:
- Could do Breadth First Search. At each node, branch into all the possible coins that are available.
  And then keep going with remainder. 
  Complexity: O(n^(target // min))
  Partial issue: will have many paths where we recompute min number to get to coins
  Solution to that issue: can keep track of amounts we've previously seen!
- Solution: recursion / memoisation
  Complexity:
  - There are O(target) subproblems
  - And combining subproblems is O(n) work (need to take a minimum)
- Base case: f(0) = 0

Is there a way to do this bottom-up?
- Yes, but that might be extra work because we might end up computing solution for
- amounts that we might not even be able to reach
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        memo[0] = 0

        def dp(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                memo[amount] = float("inf")
                return memo[amount]

            memo[amount] = 1 + min(dp(amount - coin) for coin in coins)
            return memo[amount]

        res = dp(amount)
        res = res if isinstance(res, int) else -1
        return res