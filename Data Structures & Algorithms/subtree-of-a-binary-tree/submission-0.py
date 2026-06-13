# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Approaches:
- traverse nodes of tree, and at each node, check if subtree rooted at that node is equal to subtree
- this would be O(n * m) time, and O(m) space (if solved recursively) 
"""

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        # O(m)
        def subtreeStartsHere(root, subRoot) -> bool:
            if not subRoot and not root:
                return True
            if (
                (root and not subRoot)
                or (not root and subRoot)
                or root.val != subRoot.val
            ):
                return False
            return (
                subtreeStartsHere(root.left, subRoot.left)
                and subtreeStartsHere(root.right, subRoot.right)
            )
        
        # For every possible node, check subtreeStartsHere
        # Traverse nodes using DFS
        print(f"Root: {root.val}, Subroot: {subRoot.val}")
        print(f"  subtreeStartsHere: {subtreeStartsHere(root, subRoot)}\n")
        if subtreeStartsHere(root, subRoot):
            return True
        return (
            self.isSubtree(root.left, subRoot) 
            or self.isSubtree(root.right, subRoot)
        )
        # Traverse in order using BFS
        # Maintain Stack (O(h))

        
"""
        # Only need one subtree in tree
        if not 
        # Base case:
            # If values match and we're at leaf, return True
            # If values match and we're in middle, return True & keep searching
            # False if:
                # values don't match 
            # Branch dead if
                # values don't match 

        if root.val != subRoot.val:
            return (
                isSubtree(root.left, subRoot)
                or isSubtree(root.right, subRoot)
            )

        return (
            isSubtree(root.left, subRoot)
            or isSubtree(root.right, subRoot)
            or (
                root.val == subRoot.val
                and isSubtree(root.left, subRoot.left)
                and isSubtree(root.right, subRoot.right)
            )
        )
"""
        



