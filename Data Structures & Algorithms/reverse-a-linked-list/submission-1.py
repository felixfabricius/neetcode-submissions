# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        previous_node = None
        node = head
        while True:
            # Save pointer to next node
            next_node = node.next
            # Update pointer
            node.next = None if previous_node is None else previous_node
            # Update previous node
            previous_node = node
            
            if next_node is None:
                return node
            # Update node
            node = next_node # node.next would produce an error here, since we've already modified the pointer
