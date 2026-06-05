import math

class Solution:
    def evaluate_k(self, piles: List[int], k: int) -> int:
        h = 0
        for pile in piles:
            # How to implent ceil(pile / k) using standard Python?
                # Answer (from GPT): ceil(a / b) (at least for positive integers) is (a + b - 1) // b
            #h += pile // k 
            #if pile % k > 0:
            #    h += 1
            h += math.ceil(pile / k)
        return h
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bananas = 0
        max_pile = 0
        for pile in piles:
            bananas += pile
            if pile > max_pile:
                max_pile = pile
        
        # Minimum plausible k: ceil(sum of all bananas / h) - again: how to implement ceil?
        min_k = max(bananas // h, 1)

        # Maximum plausible k: 
        max_k = max_pile

        # Start at minimum, keep increasing (using ceil) until we find one that works
        # For that k, check k - 1 to determine if answer is k - 1 or k.
        # The idea behind this is the following:
            # Increasing k by factor x can decrease time to AT BEST 1/x.
            # More generally, for x>= 1, 1/x ceil(pile / k) <= ceil(pile / xk) for every pile, so this also holds for the sum
            # Why is this true? As denominator increases, the number of cases where we need to round up to a full hour
            # also increase. -> k and h aren't perfectly antiproportional.

            # Unfortunately this is not  true.
            # Could easily think of an example, where a very small increase in k removes many "remainders",
            # and so has a large impact on required hours.
        
        # So perhaps instead:
            # Find a relatively high k that does not work
            # And then a relatively low k that does work
            # And then use binary search in between those 2.

        # Need to store last try and whether we have been successful yet:
        successful = False
        k = min_k
        prev = min_k
        #print(f"Min k: {min_k}")
        #print(f"Max k: {max_k}")
        i = 1
        while not successful:
            res = self.evaluate_k(piles, k)
            #print(f"Iteration {i} with k = {k}")
            #print(f"  Hours required: {res}")
            # Use ceiling for k.
            if res > h:
                # This is equivalent to ceil(k * res / h)
                #k = (k * res + h - 1) // h
                prev, k = k, math.ceil(k * res / h)
                #print(f"Since res / h = {res / h}, updating k to {k}.")
                i += 1
            else:
                successful = True
        
        

        # Binary search between prev and k
        a = prev
        b = k

        #print(f"\nLower bound: {a}\nUpper bound: {b}")
        while a <= b:
            c = a + (b - a) + 1 // 2
            #print(f"\nc: {c}")
            res_c = self.evaluate_k(piles, c)
            # This should only happen if c > 1
            if c > 1:
                res_c_minus = self.evaluate_k(piles, c - 1)
            else:
                return c

            # Different cases
            if res_c > h:
                a = c + 1
            elif res_c <= h and res_c_minus > h:
                return c
            else:
            #elif res_c <= h and res_c_minus <= h:
                b = c - 1    
        #return k if self.evaluate_k(piles, k - 1) > h or k == 1 else k - 1


"""
Some general thoughts:

# When do we start the binary search? Maybe at the very start?


        # Note that not all k within this range are equally likely, especially at the upper end range
        # of plausible k, the range is going to become more sparse. (More k are going to map to same hours.)
        # Therefore, binary search within the entire plausible range does not seem the most efficient.
        # (Would perhaps be placing too much weight on the upper half.)
        # And also: we could incorporate how far off we are with our k.



        # Challenge: how to choose which k to try?
            # Naive: linear. Start at one, then increment
            # Better (in the worst case, but perhaps not on average): binary search across the plausible range
            # Better: binary search across the TRULY PLAUSIBLE RANGE, which includes just the minimum k to finish in 
                # a given amount of hours
                # but: how to identify this truly plausible range?
            # Also potentially valuable: how can we incorporate information from one evaluation to properly update k?
                # (And can we ensure that we don't play ping pong when doing this)
                # Suppose that my goal is h = 4
                # And I do an evaluation and get h = 8.
                # If I doubled k, what would happen?
                    # My improvement in h would be <= factor 2 I think.
                    # Why precisely? 
                        # need to show that ceil(pile / k) <= 2 * ceil(pile / 2k) 
                            # (yeah, this is intuitively true because as you increase the denominator in the fraction)
                            # a greater domain of numbers maps to one ceil. you lose more. (Could try make this more rigorous, 
                            # but I'm quite confident about this.)
                # Similarly, if I halved k (which might not always be possible exactly if number is odd), then
                    # the time penalty would be <= factor 2
        # And this would seem to apply for ANY factor (not just double or half).

        # Maybe this way if I start with a really low value, and then multiply by how far I'm off, I could do pretty well!
        # But there's some risks. E.g. suppose there's a long stretch of ks with equal values, that are very close to the target value
        # Then i would only make very small improvements there.

        # Suppose we've hit the correct h. How do we efficiently find the minimum k with which we can achieve that h?
        # Not super obvious. Could do a linear search here. (But that would become ugly in terms of complexity, because this -> O(n),
        # where n is width of interval with plausible ks

        # Another thing we might want to use:
            # Disaggregated information about how long we're taking for each pile
        
        # Maybe we can distribute the k across the different piles somehow?
            # If one pile <= half of another pile, then will need <= half of the hours. (Is this true? No, not quite I think)
            # Instead: if one pile double that of another pile it will need between (inclusive) same amount and double the amount
            # of hours.
            # If one pile less than another pile, it will need leq number of hours.
        
        # So suppose I have a k that works. Even if I get exactly the correct amount of hours, could be that a lower k is possible.
        # If I have a k that works and a k that doesn't work, I could binary search within that range?
        # Goal of that binary search would be to find the lowest k that works.
            # A k is the lowest k that works, if for that k, hours <= h goal
            # And for 1 k less, hours >= hour goal 
        # How can we apply binary search to that?
            # Try middle of range. If k works, then try lower k (half that range)
            # If that k doesn't work, then go up again etc.
            # Stop once 

            # We're trying to find a k that doesn't work with a k that works right next to it.
            # So we're basically trying to find the highest k that doesn't work.
            # Could do this literally log_2 n times until we arrive at just one option. And then go k + 1 from there.
            # (Or alternatively, evaluate 2 different ks (k and k + 1)) at each iteration?

        # Minimum k is going to satisfy: 
"""
        