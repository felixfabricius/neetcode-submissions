# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Implementation 1:
        - Create function "height" which recursively computes height of the left and right subtree
        - Then at each call of isBalanced, call this function to compute heights.
          Also call isBalanced recursively.
        
        Complexity:
        Time:
        - height(root) = O(n) without any balance
        - and there are O(n) iterations (we also call isBalanced recursively)
        -> time complexity is O(n^2)

        Space:
        - Recursion stack: O(n)
        
        def height(root):
            if not root:
                return 0    # could also return -1 to agree with MIT course height definition
            return max(height(root.left), height(root.right)) + 1

        # Could call the height function recursively and keep track of a False result
        if root is None:
            return True
        if height(root.left) - height(root.right) not in [-1, 0, 1]:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        """
        """
        Improved implementation:
        Inefficiency of the above implementation is that when we compute height, we could
        immediately compare the heights.
        Challenge: isBalanced returns a bool, so we do need some other function (need to keep track of
        heights somehow.)
        How about: 
        - we use height function to return either an integer or a bool.
        - integer if everything up to now was balanced, bool otherwise. (Might be an issue with "False" and 0.)
        - could alternatively also do some conditional logic where we make height negative if not balanced.
          and then keep it that way. 
        """
        def height(root):
            if not root:
                return 0    # could also return -1 to agree with MIT course height definition
            if (
                height(root.left) >= 0 and height(root.right) >= 0 
                and height(root.left) - height(root.right) in [-1, 0, 1]
            ):
                return max(height(root.left), height(root.right)) + 1
            return -1

        # Could call the height function recursively and keep track of a False result
        if height(root) >= 0:
            return True
        return False
        