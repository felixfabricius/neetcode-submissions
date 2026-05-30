# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        One way to do this:
        prev = None
        first = None # remains None if both pointers are empty
        while list1 is not None or list2 is not None: # this is identical to first_A is not None or first_B is not None
            if list1 is None:
                if prev is not None:
                    prev.next = list2
                    return first
                else:
                    return list2
            elif list2 is None:
                if prev is not None:
                    prev.next = list1
                    return first
                else:
                    return list1
            elif list1.val <= list2.val: # how do comparisons work with None types? Answer: they don't.
                next1 = list1.next
                if prev is not None:
                    prev.next = list1
                else:
                    first = list1
                prev = list1
                list1 = next1
            else:
                next2 = list2.next
                if prev is not None:
                    prev.next = list2
                else:
                    first = list2
                prev = list2
                list2 = next2
        return first
        """
        # Exercise: can I write this recursively instead of using the while loop.
        '''Recursion base cases'''
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        # Could potentially include an else statement here
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2

            