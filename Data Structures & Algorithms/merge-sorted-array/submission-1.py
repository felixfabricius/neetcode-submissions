class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Comments upon completion: merging from end would be better than
        merging from the front! Compare largest remaining elements of both
        arrays.
        """
        
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Approach 1:
        # Do classical merge step from merge sort, and everytime we select
        # an element from nums2, shift all the necessary elements from nums1
        # Complexity:
            # Space: O(1)
            # Time: n + m steps; and for each of the m steps,
            # potentially need to shift up to O(n + m) elements, which
            # dominates time. So:
            # O(n + m(n + m))
        
        # Is there a better way to do this, which doesn't require the
        # frequent shifting of all the elements from nums1?
        # What about:
        # shifting all the elements in nums1 to the back once, and then
        # filling array up from the front.
        # This has time complexit O(n (for the shifting) + n + m), which is better

        # Shift elements from nums1 to back of array
        for i in range(m):
            nums1[len(nums1) - 1 - i] = nums1[m - 1 - i]
            # Not even necessary to set nums1[m - i] to zero I think
        
        # New starting index of the valid numbers within nums1 is n
        # Merge
        i, j = 0, 0
        while i + j < len(nums1):
            # If nums2 is exhausted, or nums1 is not exhausted and 
            # next element from nums1 is smaller than from nums2
            if (j >= n) or (i < m and nums1[n + i] < nums2[j]):
                nums1[i + j] = nums1[n + i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1

    
