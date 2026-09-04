from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        """
        Approach

        When should the program return a value?
        - Either when students or sandwiches length is zero
        - Or when every student has looked at the current sandwich

        What tasks does interface need to solve?

        - sandwiches.popleft()
        - students.popleft(); students.append() (or append)
        """

        sandwich_q = deque(sandwiches)
        student_q = deque(students)

        rejected = 0
        while len(sandwich_q) > 0:
            if rejected == len(student_q):
                return len(student_q)
            if sandwich_q[0] == student_q[0]:
                sandwich_q.popleft()
                student_q.popleft()
                rejected = 0
            else:
                student_q.append(student_q.popleft())
                rejected += 1

        return 0 