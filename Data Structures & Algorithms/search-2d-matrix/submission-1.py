class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
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
        """

        # Approach 2
        # Binary search, but on - effectively flattened - matrix
        # This allows us to perform just a single binary search
        # Imagine that matrix is sorted array of length m * n 
        # Indexing: to access the correct element in the matrix given we want say 
        # element c (zero-indexed) in the
        # flattened array, can do: 
            # row index: (c - 1) // n. Reason for c - 1: zero-indexing. 
            # No, THAT'S BS. Just use c!! 
            # e.g. if n = 8, then 8th element in flattened index would actually
            # be the first element in the second row.
            # Yes. But if c = 8, then we also want that element, because c = 9 means we want
            # the ninth element.
            # column index: c % n (here we want to use the zero-indexing in our favour)

        # Why might this be preferable? Intuitively we might get better constants than before.
        # But why?
        m = len(matrix)
        n = len(matrix[0])

        a = 0
        b = m * n - 1

        while a <= b: 
            c = a + (b - a) // 2
            row = c // n
            col = c % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                b = c - 1
            else:
                a = c + 1
        return False




