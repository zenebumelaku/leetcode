class Solution(object):
    def countStudents(self, students, sandwiches):
        from collections import deque
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        rotations = 0  # count consecutive rotations
        
        while students and rotations < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                rotations = 0  # reset rotations
            else:
                students.append(students.popleft())  # move front student to end
                rotations += 1
        
        return len(students)
