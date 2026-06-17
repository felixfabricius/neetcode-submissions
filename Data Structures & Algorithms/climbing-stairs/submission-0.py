"""
Approach:
- we know that f(n) = f(n - 1) + f(n - 2)
- we have base cases: f(1) = 1 and f(0) = 1
- therefore this is identical to calculating fibonacci sequence

Can solve this using top-down dynamic programming, with cache.
Or bottom up dynamic programming with simple iteration.
Let's implement the cached version.
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        f = {}
        f[0] = 1
        f[1] = 1
        
        def calc_number_of_ways(i):
            if i not in f:
                # note that this automatically takes into account the base case
                # reason: f[0] and f[1] are in f
                f[i] = calc_number_of_ways(i - 1) + calc_number_of_ways(i - 2)
            return f[i]
        return calc_number_of_ways(n)
        