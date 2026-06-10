# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
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
        
        