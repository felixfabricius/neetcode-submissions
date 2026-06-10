class Solution:
    """
    #    Brute force approach:
    #    - Loop over the possible lengths of a subset (0 to len(nums))
    #    - For each possible length, get all subsets of that length:
    #      - For length m, could possibly create m for loops?
    #      - And then if we're careful with the indices, we'd get all the possible combinations
    #    - Alternatively: there are 2^n subsets. Those can be represented by a n-digit binary
    #      number. Perhaps we can loop from 0 -> 2^n and then add the numbers which are activated
    #      with each of those binary digits?
    #    
    #    Can I manually translate an integer into its binary form? Yes.
    #    -> Loop over all the possible binary representations (can represent as list.)
    #    And then correspondingly add numbers.

    # Complexity:
        # Time: 
        # For each possible binary number O(2^n):
            # Compute binary representation: O(n)
            # Loop through list and add correct numbers: O(n)
        # -> O(n * 2^n)
        # Space:
        # Store binary representation of length n, and the output (which doesn't count, though)
        # -> O(n)

    # Can improve this by not explicitly converting to binary!
    
    def convert_to_binary(self, num: int, n: int) -> list[int]:
        binary_representation = []
        for i in range(n - 1, -1, -1):
            if num >= 2 ** i:
                binary_representation.append(1)
                num -= 2 ** i
            else:
                binary_representation.append(0)
        
        return binary_representation

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for i in range(2 ** n):
            binary_representation = self.convert_to_binary(i, n)
            print(f"i: {i}, binary: {binary_representation}\n")
            assert len(binary_representation) == n
            subset = []
            for j in range(n):
                if binary_representation[j]:
                    subset.append(nums[j])
            # Better than manually computing binary representation:
            # if i & (1 << j):
            #   subset.append(nums[j])
            # How does this evaluate: 1 << j creates a binary number with
            # just the jth bit (starting at 1st bit, i.e. 0) turned on.
            # Then i & that binary number will evaluate to 1 iff the jth bit in i is 
            # also turned on. Otherwise it evaluates to zero. 
            # & is bitwise and operator.
            # This is really neat!
            res.append(subset)
        return res
    """
    """
    Can I do better?
    What seems inefficient about the above approach?
    - The fact that we're often times adding the same start of a subset again and again.
      Would perhaps be better to start with a given subset, and then from that given subset to
      add everything else.
      Example: let m = n / 2.
      1. Enumerate each of the possible subsets among first m digits. Time: O(2^m) * O(m)
      2. And then for each of those 2^m subsets, again add each of the possible ensuing subsets
         -> need to square the above complexity.
      Total time complexity:
      2^m * (O(m) + O(2^m * O(m)))
      = O(2^(2m) * O(m)) = O(2^n * n/2)
      So not much better.
    
    Can I use backtracking and make use of trees? This seems to take this above idea to the extreme.
    -> best possible constants?  
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Recursive implementation
        # Complexity:
            # Time: O(2 ** n * n)
            # Space: 
                # there are maximally n recursive calls (1 path) alive at the same time
                # memory taken up by each of those recursive calls is O(1) since
                # subset is modified in place
                # note that this is not true if we do res += inside the recursive function.
                # this would require copying. 
                # instead, use list.extend() (or list.append() twice)
        res = []
        n = len(nums)

        def append_to_subset(subset: list[int], i: int):
            if i == n - 1:
                # res += [subset, subset + [nums[i]]]
                # This doesn't work. Reason: += is counted as an assignment operator.
                # Given assignment, Python treats res as a local variable and attempts to read it.
                # But it can't find a local variable named res, so errors.
                res.extend([subset, subset + [nums[i]]])
                return
            append_to_subset(subset, i + 1)
            append_to_subset(subset + [nums[i]], i + 1)
        
        append_to_subset([], 0)

        return res
