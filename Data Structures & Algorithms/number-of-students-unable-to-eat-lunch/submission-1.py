class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        def ableToEat(students: List[int], sandwiches: List[int]) -> bool:
            if students[0] != sandwiches[0]:
                if set(students) == {0}:
                    if set(sandwiches) != {0}:
                        return False
                if set(students) == {1}:
                    if set(sandwiches) != {1}:
                        return False
            return True
        while len(students) > 0 and ableToEat(students, sandwiches):
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
        return len(students)
