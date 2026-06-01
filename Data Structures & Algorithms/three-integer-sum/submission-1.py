class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        1. Sort nums
        2. For each num in nums with index i:
            - initialise two pointers to the right of num (at i + 1, and len(nums) - 1)
            - calc sum. if sum too large, then decrement the right  pointer.
              if too small, then increment the left pointer
              This approach won't miss any valid triple
            - if match: increment left pointer & decrement right pointer
            - repeat this until left pointer is no longer lower than right pointer
        3. To ensure uniqueness of added tuples:
            - We cannot simply add any triple and then deduplicate at the end.
              Reason: There are n choose 3 = O(n^3) possible triplets. And any approach
              that deduplicates list of triples would have to at least look at each triple
              once -> would be at least O(n^3)
            - Therefore: avoid adding duplicates from the start.
                a. After finishing the two pointer approach for num with index i, 
                   increment i. Increment it until num increases. If num is still identical,
                   any valid triplet we identify would already have been identified in a 
                   previous iteration
                b. After match: increment low pointer & decrement high pointer. Reason: if we
                   only changed one of them, then this could only ever be a match in case of
                   duplicate.
                c. If incrementing low pointer and decrementing high pointer -> same values (for both),
                   then increment and decrement again.
        
        I think it would probably be possible to solve the while loop recursively.
        Out of interest, let's try think of an algorithm for that:
        1. Suppose we have a function, which for a given num and existing i and j pointer
           returns all the valid triples with that num.
        2. Then that function could be expressed using function call with the pointers being
           more inwards (or at least one of them?) + evaluating whether the current option
           is a valid triple.
        
        Why this doesn't make sense to do:
        - Not sure how to deduplicate
        - Would take a lot more space. Because would save the list of triplets for each
          intermediate function call
        """
        nums.sort()

        # Keep track of current leftmost num (so we can increment accordingly),
        # as well as of current lower value in valid triple and upper value 
        # in valid triple, so we can move the two pointers if necessary to avoid
        # duplicates
        num = -10^5 - 1
        output = []

        for i in range(len(nums) - 2):
            # Skip this iteration to avoid adding duplicates
            if nums[i] == num:
                continue
            num = nums[i]

            j = i + 1
            k = len(nums) - 1

            # Initialise lower and upper variables.
            # Used to avoid adding duplicates.
            lower = nums[j] - 1
            upper = nums[k] + 1

            while j < k:
                if nums[j] == lower and nums[k] == upper:
                    j += 1
                    k -= 1
                    continue
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    lower = nums[j]
                    upper = nums[k]
                    j += 1
                    k -= 1
                elif res > 0:
                    k -= 1
                else:
                    j += 1

        return output

