# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        # Complexity: DFS with updated bounds.
        #    - O(n) time (checking <= 2n + 1 nodes)
        #    - O(h) space 
        
        def valid(node, a, b):
            if not node:
                return True
            if not a < node.val < b:
                return False
            return (
                is_valid_bst(node.left, a, min(b, node.val))
                and is_valid_bst(node.right, max(a, node.val), b)
            )

        return valid(root, -1001, 1001)
        # Alternatively, could also pass float("-inf"), float("inf") here
        # (If we didn't know the bounds)
        """

        # BFS
        # Idea: for each node store bounds
        nodes = [(root, float("-inf"), float("inf"))]
        while len(nodes) > 0:
            curr = nodes.pop()
            if not curr[0]:
                continue
            if not (curr[1] < curr[0].val < curr[2]):
                return False
            nodes.extend([
                (curr[0].left, curr[1], min(curr[2], curr[0].val)),
                (curr[0].right, max(curr[1], curr[0].val), curr[2])
            ])
        return True
