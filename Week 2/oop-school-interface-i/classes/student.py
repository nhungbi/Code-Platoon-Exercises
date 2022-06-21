import os
import csv
from classes.person import Person

class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        Person.__init__(self, name, age, password, role)
        #can also use super().__init__(name, age, password, role)
        self.school_id = school_id

    def all_students():
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        list_students = []
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile) #read row as dictionary, header denotes the key
            for row in reader: #row is a dict of with parameters to create Student
                list_students.append(Student(**row))

        return list_students

# x = {'name': 'Lisa', 'age': '25', 'role': 'Student', 'school_id': '13345', 'password': 'xx '}
# print(Student.all_students())



# student_info = {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# x = Student(**student_info)
# print(x.name)
# the ** before student_info turns this: 
    # {'name' : 'Diana', 'password' : 'password', 'school_id' : 12345, 'age' : 17, 'role' : 'Student'}
# Into this:
    #  name='Diana', password='password', school_id=12345, age=17, role='Student'

