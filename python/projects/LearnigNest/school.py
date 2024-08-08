class School:
    school_name: str = "The Learning Nest"
    students: list[dict] = []

    @property
    def total_students(self):
        return len(self.students)

    @classmethod
    def registration(cls, student: dict):
        cls.students.append(student)

    @classmethod
    def delete_student(cls, student: dict):
        cls.students.remove(student)

    @classmethod
    def student_info(cls, student: dict):
        return cls.students.index(student)
