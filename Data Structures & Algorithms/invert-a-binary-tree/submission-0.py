# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Inverting a tree:
- each node's left child becomes its right child and vice versa
- Does the order in which we traverse the tree matter? Don't think so.
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = left
        return root
