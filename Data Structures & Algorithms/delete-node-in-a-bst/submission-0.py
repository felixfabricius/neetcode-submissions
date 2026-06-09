# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Might be annoying to implement recursively with this function signature because we 
        would also need to keep track of parent. (So we can change pointers.)

        Therefore, do iteratively.

        If curr.val = key & current node has no children, then simply delete it.
        Delete means: change pointer from parent.

        If curr has two children, then need to turn one of the children into new parent.
        Which one of the two? Need to maintain traversal order.

        - If root.val == key, then 
        """
        curr = root
        prev = None
        while not curr is None:
            if curr.val == key:
                if curr.left is not None and curr.right is not None:
                    # Replace curr with its in-order successor.
                        # Find the node to replace curr with
                        # Remove link of the parent node to curr (must avoid cycles)
                        # Give curr the links 
                    candidate = curr.right
                    candidate_parent = curr
                    i = 1
                    while candidate.left is not None:
                        candidate_parent = candidate
                        candidate = candidate.left
                        i += 1
                    # Remove pointer from candidate parent to candidate:
                    # If i > 1, then candidate is left child of candidate parent
                    # Note that it's possible for the candidate node to have right children.
                    if i == 1:
                        candidate_parent.right = candidate.right
                    else:
                        candidate_parent.left = candidate.right
                    
                    # Adequately modify pointers of candidate
                    candidate.left = curr.left
                    if i > 1:
                        candidate.right = curr.right
                    else: 
                        # i == 0: can't point candidate.right to curr.right because curr.right = candidate
                        # in this case, can simply keep pointer the same. Note that candidate.right won't
                        # have a left child anyways
                        candidate.right = candidate.right

                    # Adequately modify pointers to candidate
                    if prev is None:
                        return candidate # candidate is the new root
                    else:
                        if prev.val > curr.val:
                            prev.left = candidate
                        else:
                            prev.right = candidate
                        return root
                # If the sought node has either none or one child, just change pointer from
                # previous node to that node
                else:
                    replacement = curr.left if curr.left is not None else curr.right
                    if prev is None:
                        return replacement
                    else:
                        if prev.val > curr.val:
                            prev.left = replacement
                        else:
                            prev.right = replacement
                        return root
            elif curr.val < key:
                prev = curr
                curr = curr.right
            elif curr.val > key:
                prev = curr
                curr = curr.left

        return root