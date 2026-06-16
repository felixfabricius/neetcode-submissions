"""
Approach:
- a graph is a valid tree if it contains no cycles
- and if it also contains no disconnected nodes

Suppose I had adjacency list:
- Then: starting at one node, and doing either BFS or DFS to all other nodes,
  I must never arrive at the same node twice
  (or: if we count the undirected edges twice, must arrive at every node exactly twice;
  no: this isn't a viable alternative because can have nodes with variable amounts of edges)
  Tricky here: may have the edge presented in the wrong way.
  Therefore: maybe initially build an adjacency list? 
  And that way: can attribute edge to both of the nodes, and then also pop it from both nodes
  as soon as we traverse it once.

Complexity of this:
- build adjacency list:
    - time: O(n + E) because one entry per node
    - space: O(n + E)
- Once we have adjacency list:
    - Space: O(n) to keep track of number of vertices we've seen + O(E) for BFS 
    - Time: O(E)
-> in total: time O(E) and space O(n + E)
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build adjacency list
        adj_list = {}
        for a, b in edges:
            adj_list[a] = adj_list.get(a, set()) | {b}
                # How to add to a set, not in-place? use union
            adj_list[b] = adj_list.get(b, set()) | {a}
        
        # Keep track of vertices we've seen
        seen = {0}
        
        # Loop through all the edges, starting with the first.
        # If either: we arrive at same node twice, or we haven't arrived at a node, 
        # our graph does not constitute a valid tree.
        queue = deque([0])
        
        while len(queue) > 0:
            a = queue.pop()
            for b in adj_list.get(a, set()):
                if b in seen:
                    return False
                adj_list[b].remove(a)
                    # Recall: to remove element from set, can use
                    # .remove() or .discard().
                    # .remove() will raise a KeyError if element not in set
                    # For dictionary: can do del my_dict["key"] or my_dict.pop("key")
                    # For safe deletion: my_dict.pop(key, None)
                seen.add(b)
                queue.append(b)

        return len(seen) == n