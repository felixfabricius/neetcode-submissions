# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return new_head

    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # This special case might not be needed.
        if n == 1:
            return
        
        head_2_idx = (n + 1) // 2

        # Find head 2 and then detach pointer from last element of first list too fully separate the lists.
        curr = head
        for i in range(head_2_idx - 1):
            curr = curr.next
        head_2 = curr.next
        curr.next = None
    
        # Reverse the second list. Let's do this recursively.
        # (Even though one could probably do this with lower space complexity w/o recursion.)
        # Note that in the case where n equals 1, head_2 is None, and so reverseList won't do anything.
        new_head_2 = self.reverseList(head_2)

        # Merge the two lists
        curr_1 = head
        curr_2 = new_head_2

        i = 0
        while True:
            if i % 2 == 0:
                hanging_1 = curr_1.next
                curr_1.next = curr_2
                curr_1 = hanging_1
            
            else:
                hanging_2 = curr_2.next
                curr_2.next = curr_1
                curr_2 = hanging_2
            
            i += 1
            
            if curr_1 is None and curr_2 is None:
                break


        