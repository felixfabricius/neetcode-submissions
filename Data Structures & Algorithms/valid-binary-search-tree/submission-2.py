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
            # Better syntax: node, left, right 0 nodes.pop()
            # Immediately unpack the tuple
            if not curr[0]:
                continue
            if not (curr[1] < curr[0].val < curr[2]):
                return False
            nodes.extend([
                (curr[0].left, curr[1], min(curr[2], curr[0].val)),
                (curr[0].right, max(curr[1], curr[0].val), curr[2])
            ])
        return True

        # Note on various ways to implement BFS:
        # Makes sense to only append children if they exist: better constant for space complexity
        # If tree is balanced, then stack approach is better than queue approach.
        # But note: Stack approach does not correspond to BFS!!! Stack approach is DFS.
        # We pursue one path fully before pursuing the next... 
        # Though note that this is only in order DFS if we add the right child before the left child.
        
        # BFS space complexity (using queue): O(n). Which for balanced tree will be worse than
        # the O(h) recursion stack.