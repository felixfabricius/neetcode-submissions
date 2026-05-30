# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach 1:
        - store a pointer to each of the heads of the list  (that is literally lists array)
        - find minimum across all the heads (O(k))
        - move pointer from previous link (if exists to the minimum)
        - move pointer for that k one further
        - could recurse here. (Again: how to?)
        - Only select a node if it is not None. If there is only one that isn't None, can return.
        """
        prev = None
        first = None
        k = len(lists)
        while True:
            none_counter = 0
            min_val = 1000 # based on constraints. there will be no larger values
            min_idx = None
            for i in range(k):
                if lists[i] is None:
                    none_counter += 1
                elif lists[i].val <= min_val:
                    min_val = lists[i].val
                    min_idx = i
            if min_idx is None:
                return first
            if prev is not None:
                prev.next = lists[min_idx]
                prev = lists[min_idx]
            else:
                first = lists[min_idx]
                prev = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            if k - none_counter <= 1:
                break
        
        return first
                