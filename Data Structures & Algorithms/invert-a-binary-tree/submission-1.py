# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

"""
Inverting a tree:
- each node's left child becomes its right child and vice versa
- Does the order in which we traverse the tree matter? Don't think so.
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        # DFS approach
        if not root:
            return root
        left = self.invertTree(root.left)
        root.left = self.invertTree(root.right)
        root.right = left
        return root
        """
        # BFS approach
        nodes = deque([root])
        while len(nodes) > 0:
            for _ in range(len(nodes)):
                node = nodes[0]
                if not node:
                    nodes.popleft()
                    continue
                elif node.left or node.right:
                   nodes.append(node.left)
                   nodes.append(node.right)
                   node.left = nodes[-1]
                   node.right = nodes[-2]
                nodes.popleft()
        return root
    
    
