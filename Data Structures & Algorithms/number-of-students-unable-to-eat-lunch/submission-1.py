from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional(ListNode) = None):
        self.val = val
        self.next = next


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        An approach based simply on counting number of available square sandwiches
        and number of students with that preference, does not work because 
        the order of the sandwiches matters. It's possible e.g. that there are 
        3 sandwiches left, the top one is a square sandwich and the next two are 
        round ones, but all 3 students left in the queue want a round one.
        """
        # Build linked list for the students
        next = None
        for i, student in enumerate(students[::-1]):
            next = ListNode(student, next)
            if i == 0:
                tail = next
        head = next

        # For the sandwiches, there is no need to build a linked list,
        # but I do want to be able to remove in constant time.
        # Using static array, this means I must remove from the end.
        # Therefore, need to reverse sandwiches.
        sandwiches = sandwiches[::-1]
        
        # Q: does this way of reversing the list require an extra O(n) space?
        # I don't think it would necessarily have to.
        # Even though it would generally be possible to reverse in place, I don't think
        # this is happening here.
        # Can instead use the list.reverse() method to do that!

        # Start the lunch queue
        # In this case we have cycled through all the students and 
        # no one wanted the sandwich on top of the stack
        first = head
        while len(sandwiches) > 0:
            if head.val == sandwiches[-1]:
                head = head.next
                first = head
                sandwiches.pop()
            else: 
                if head.next is None or head.next == first:
                    break
                tail.next = head
                head = head.next
                tail = tail.next
                tail.next = None
               
        return len(sandwiches)

        

