"""Kindergarten Garden exercise"""

class Garden:
    """A kindergarten plant garden"""

    plant_names = {"V": "Violets", "R": "Radishes", "G": "Grass", "C": "Clover"}

    def __init__(self, diagram, students=None):

        if students is None:
            self.students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",\
                             "Ileana", "Joseph", "Kincaid", "Larry"]
        else:
            if not isinstance(students, list):
                raise TypeError("Student list must be a list of strings.")
            for student in students:
                if not isinstance(student, str):
                    raise TypeError("Student names must be strings.")
            self.students = sorted(students)
        if not isinstance(diagram, str):
            raise TypeError("Diagram must be a string.")

        self.pots = [list(row) for row in diagram.splitlines()]

    def plants(self, student):
        """The student's plants.
 
        :param str student: The student's name.
        :raises TypeError: Raised when the name is not a string.
        :raises ValueError: Raised when the student is not in the class roster.
        :return list[str]: The student's plants.
        """

        if not isinstance(student, str):
            raise TypeError("Student name must be a string.")
        if student not in self.students:
            raise ValueError("Student not in class roster.")

        student_number = self.students.index(student)

        return [
            self.plant_names[row[plant]] for row in self.pots
            for plant in range(2*student_number, 2*student_number+2)
            ]
