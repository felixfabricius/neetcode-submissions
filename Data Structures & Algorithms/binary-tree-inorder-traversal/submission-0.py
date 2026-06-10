# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if not root:
            return []
        nodes += self.inorderTraversal(root.left)
        nodes.append(root.val)
        nodes += self.inorderTraversal(root.right)
        return nodes