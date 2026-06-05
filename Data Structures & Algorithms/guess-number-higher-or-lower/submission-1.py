# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

"""
Notes upon completion: 
- based on solution, can also implement "ternary search", where we make two guesses each time (at one third and two thirds of search space)
- and then based on the results, we can eliminate two thirds of the search space each time. (we know which third the number is in)

How would this compare to binary search?
- Suppose 'naive' implementation where we always call function twice: I think this would simply be worse than binary search 
(by a constant factor) because we're doing two 'suboptimal' calls (each call to function helps us reduce search space) by one third;
whereas for binary search, it would be 1/2. But then this depends a bit on relative cost of calling this function compared to cost
of other operations each iteration (e.g. updating l, h, m)
- Suppose we do this in a 'smart' way, where we only call function a second time, if result from first call is such that
this is plausible (e.g. if see that number is less than the 2/3rd point, then we try 1/3 point)
Then - assuming uniform prior over where number is - expected reduction in search space per call to function is going to be 
1/3 (probability of landing on very outside) * 2/3 (reduction given this) + 2/3 * 1/3 = 1/2
(this is approximate because we ignore fact that we discard m as well if no match)
"""

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n

        while l <= h:
            m = l + (h - l) // 2
            feedback = guess(m)
            if feedback == 0:
                return m
            elif feedback == 1:
                l = m + 1
            else:
                h = m - 1
        
        raise RuntimeError("Unreachable Code Reached")