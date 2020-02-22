from collections import defaultdict
import numpy as np

class School:

    def __init__(self):
        self.grades = defaultdict(list)

    def add_student(self, name, grade):
        self.grades[grade].append(name)

    def roster(self):
        result = np.empty(0,dtype=str)
        for grade in sorted(self.grades.keys()):
            result = np.append(result,self.grade(grade))

        return list(result.flatten())

    def grade(self, grade_number):
        if self.grades.get(grade_number) is not None:
            return sorted(list(self.grades.get(grade_number)))
        else:
            return list([])
