from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(cls):
        students = Student.objects() #a list of students instances
        output = []
        for i in range (len(students)): #student is an instance
            output.append(f'{i+1}. {students[i].name} {students[i].school_id}')
        
        string_output = '\n'.join(output) #join array into a single string to print
        return string_output

    def find_student_by_id(self, student_id):
        """
        Given a student id, return the student with the matching id.
        """
        students = Student.objects()
        for student in students:
            if student.school_id == student_id:
                return student