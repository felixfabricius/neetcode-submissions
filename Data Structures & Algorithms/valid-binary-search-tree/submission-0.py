# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Complexity:
            - O(n) time (checking <= 2n + 1 nodes)
            - O(h) space 
        """
        def is_valid_bst(node, a, b):
            if not node:
                return True
            if not a < node.val < b:
                return False
            return (
                is_valid_bst(node.left, a, min(b, node.val))
                and is_valid_bst(node.right, max(a, node.val), b)
            )

        return is_valid_bst(root, -1001, 1001)
