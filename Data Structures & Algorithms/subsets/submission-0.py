class Solution:
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
        """
        Brute force approach:
        - Loop over the possible lengths of a subset (0 to len(nums))
        - For each possible length, get all subsets of that length:
          - For length m, could possibly create m for loops?
          - And then if we're careful with the indices, we'd get all the possible combinations
        - Alternatively: there are 2^n subsets. Those can be represented by a n-digit binary
          number. Perhaps we can loop from 0 -> 2^n and then add the numbers which are activated
          with each of those binary digits?
        
        Can I manually translate an integer into its binary form?
        Yes.
        """
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
            res.append(subset)
        return res
