class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Approach 1: 
        # First use binary search to find correct row
        # Then use binary search to find correct element within row
        # This has time compleity O(log m) + O(log n) = O(log(m * n))
        m = len(matrix)
        n = len(matrix[0]) 

        # Find correct row.
        # Logic to compare rows:
            # Row might be correct if first value in row is leq value and last
            # value in row is geq value
        a = 0
        b = m - 1
        plausible_row = None    

        while a <= b and plausible_row is None:
            c = a + (b - a) // 2
            if matrix[c][0] <= target and matrix[c][n - 1] >= target:
                plausible_row = c
            elif matrix[c][0] > target:
                b = c - 1
            else:
                a = c + 1
        if plausible_row is None:
            return False

        a = 0
        b = n - 1
        while a <= b:
            c = a + (b - a) // 2
            if matrix[plausible_row][c] == target:
                return True
            elif matrix[plausible_row][c] > target:
                b = c - 1
            else:
                a = c + 1
        
        return False




