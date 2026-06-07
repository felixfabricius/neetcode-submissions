# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Approach:
        - Binary search tree property: all nodes in left subtree of a focal node have <= val,
          and all nodes in right subtree have >= value
        - This implies that if a value is smaller than a node, it must become part of its left subtree
        - This way we can traverse the tree until the node we reach does not hae a child node
          in the direction of comparison. There we can attach our node.
        - Note that without rotating our tree after, the tree will not remain balanced this way,
          so eventually we would get complexity = O(h) > O(log n)
        
        # Recursive implementation
        # Has complexity: O(h) time and O(h) memory
        if root is None:
            return TreeNode(val)
        elif val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root
        """
        # Alternative non-recursive implementation
        # With complexity: O(h) time and O(1) space
        if root is None:
            return TreeNode(val)
        # Iteration. Need to keep track of current node. 
        curr = root
        inserted = False
        while not inserted:
            if val < curr.val:
                if curr.left is None: 
                    curr.left = TreeNode(val)
                    inserted = True
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(val)
                    inserted = True
                else:
                    curr = curr.right
        return root