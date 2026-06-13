# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        # Helper function that returns:
            # 1) maximum sum of any one-directional path (modps) in subtree rooted at node 
            #    that contains node
            #    which can be computed recursively given the children
            # 2) maximum path sum of any path contained in subtree rooted at node
            #    which can be computed recursively as
            #    max(mps(node.left), mps(node.right), f(modps(node.left), modps(node.right), node.val)   
        def helper(node):
            min_value = -1001
            modps_l, mps_l, modps_r, mps_r = min_value, min_value, min_value, min_value
            
            if node.left:
                a, b = helper(node.left)
                modps_l = max(modps_l, a)
                mps_l = max(mps_l, b)
            if node.right:
                a, b = helper(node.right)
                modps_r = max(modps_r, a)
                mps_r = max(mps_r, b)
            
            modps = max(
                node.val,
                node.val + modps_l,
                node.val + modps_r
            )

            mps = max(
                mps_l,
                mps_r,
                node.val + max(modps_l + modps_r, modps_l, modps_r, 0)
            )

            return modps, mps

        return helper(root)[1]