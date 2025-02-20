"""Grade School exercise"""

class School:
    """A school's grades and students"""

    def __init__(self):
        self.grades = {}
        self.added_list = []

    def add_student(self, name, grade):
        """Adds a student to a grade.
 
        :param str name: The name of the student.
        :param int grade: The grade the student is to be added
        :raises ValueError: Raised when there are missing arguments.
        :raises TypeError: Raised when the name is not a string.
        :raises TypeError: Raised when the grade is not an integer.
        """

        if name is None or grade is None:
            raise ValueError("Missing arguments.")
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(grade, int):
            raise TypeError("Grade must be an integer.")
        if name in self.roster():
            self.added_list.append(False)
        elif grade not in self.grades:
            self.grades[grade] = [name]
            self.added_list.append(True)
        else:
            self.grades[grade].append(name)
            self.added_list.append(True)

    def roster(self):
        """Returns the complete roster, sorted alphabetically by grade.
 
        :return list[str]: The complete roster.
        """

        students = []
        for grade_no in sorted(self.grades.keys()):
            for student in self.grade(grade_no):
                students.append(student)
        return students

    def grade(self, grade_number):
        """Returns a grade's students, sorted alphabetically.
 
        :param int grade_number: The grade.
        :raises ValueError: Raised when there's no input.
        :raises TypeError: Raised when the grade is not an integer.
        :return list[str]: The grade's roster.
        """

        if grade_number is None:
            raise ValueError("Not enough arguments.")
        if not isinstance(grade_number, int):
            raise TypeError("Grade must be an integer.")
        return sorted(self.grades[grade_number]) if grade_number in self.grades.keys() else []

    def added(self):
        """Returns a list with the log of added students.
 
        :return list[bool]: A list of the results of the add student operations.
        """

        return self.added_list
