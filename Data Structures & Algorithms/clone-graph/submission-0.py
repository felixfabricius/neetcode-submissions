"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Approach:
- task is basically to traverse the graph and visit every node once
- Start with some node. Visit each of its neighbours (if not already visited; keep track via set). 
  Then for each of its neighbours: 
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        seen = {}

        def copy_node(node):
            seen[node.val] = Node(node.val)
            neighbors_copy = []
            for neighbor in node.neighbors:
                if neighbor.val in seen:
                    neighbors_copy.append(seen[neighbor.val])
                    continue
                neighbors_copy.append(copy_node(neighbor))
            seen[node.val].neighbors = neighbors_copy
            return seen[node.val]

        return copy_node(node)
                



