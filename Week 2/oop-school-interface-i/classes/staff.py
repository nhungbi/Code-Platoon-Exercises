import os
import csv
from classes.person import Person
# from person import Person

class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        Person.__init__(self, name, age, password, role)
        self.employee_id = employee_id

    def all_staff():
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../data/staff.csv")
            # path = os.path.abspath('data/staff.csv') #also works
            list_staff = []
            with open(path) as csvfile:
                reader = csv.DictReader(csvfile) #read row as dictionary, header denotes the key
                for row in reader: #row is a dict of with parameters to create Student
                    list_staff.append(Staff(**row))

            return list_staff

# print(Staff.all_staff())