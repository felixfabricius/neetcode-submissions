# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        # Naive recursion: allocate a new list at every call of the recursive function
        # Time complexity: we call the inorderTraversal() function O(n) times (max 2n times because a
        # few extra times at the leaves). Each time we call, we need to modify in place the
        # list that the parent holds. Copying over all the elements is O(n). -> Time: O(n^2)
        # Space complexity: 
        #   - Recursion stack: O(h).
        #     Reason: at any time, only all the calls from one path down the tree are alive.
        #     Suppose we finish the bottom left and then go one up and then one down to the right,
        #     Then there are still O(h) calls alive.
        #   - From storing the lists at each call:
        #     Once we have finished computing the nodes list at one node (that list is O(n) space),
        #     we need to copy it over to the parent. (which takes O(n) time).
        #     Once we've done that, we delete that O(n) list.
        #     Note that there are O(h) empty lists stored at the same time. But that can be seen as
        #     part of the recursion stack.
        
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
        - time: O(n)
        - space: O(h) = O(n) without restrictions on balance
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

        """
        How could this be done iteratively:
        - Whenever we go down, need to store previous node. To be able to go back up.
        - After we go back up, we need to go right, and then keep going down.
        - Note that it's not sufficient to store one previous node. Rather, need to store all the
          previous nodes on path I think,.
        """
