# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        # Naive recursion: 
        # - allocate a new list at every call of the recursive function
        #   -> O(n^2) space;
        #   O(n) time
        
        nodes = []
        if not root:
            return []
        nodes += self.inorderTraversal(root.left)
        nodes.append(root.val)
        nodes += self.inorderTraversal(root.right)
        return nodes
        """
        """
        Better recursion:
        - don't allocate a new list at every call of the recursive function.
          rather: append in place
        """
        res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)

        return res
