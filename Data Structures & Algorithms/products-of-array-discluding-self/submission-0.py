class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Simplest code for this: double for loop. Complexity: O(n^2).

        To get time complexity O(n), need to do some O(n) operation once & then 
        constant time operation for each element.
        Here also need to account for impact of zeroes.
        """

        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1
        if zero_count >= 2:
            return len(nums) * [0]
        elif zero_count == 1:
            return [product if num == 0 else 0 for num in nums]       
        else:
            return [product // num for num in nums]     
