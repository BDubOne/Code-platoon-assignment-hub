import csv
from person import Person

class Staff:
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(self, name, age, role, password)
        self.employee_id = employee_id

    @classmethod
    def all_members(cls):
        staff = []
        with open('./data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_staff = cls(**row)
                staff.append(new_staff)
        
        return staff
    
# Staff.all_staff()