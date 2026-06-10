# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Task: for each level, return the rightmost node
        if not root:
            return []
        
        res = []
        nodes = deque()
        nodes.append(root)

        while len(nodes) > 0:
            n = len(nodes)
            for i in range(n):
                curr = nodes.popleft()
                if i == n - 1:
                    res.append(curr.val)
                if curr.left:
                    nodes.append(curr.left)
                if curr.right:
                    nodes.append(curr.right)
        
        return res