
# class method vs instance method vs static methods

import datetime

class Employee:

    raise_amount = 1.04
    num_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_employees += 1

    # class method change raise amount
    @classmethod
    def set_raise(cls,amount):
        cls.raise_amount = amount

    # constructor parse string employee
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    # static method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    # instance method/ regular method
    def fullname(self):
        full_name = f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('youss', 'amar', 50000)
emp_2 = Employee('Joe', 'rama', 60000)

# employees defined as  string
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

my_date = datetime.date(1984, 6, 2)

print(Employee.is_workday(my_date))

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.first)
print(new_emp_1.last)
print(new_emp_1.pay)
print(new_emp_1.email)
# change raise_amount in the Class
# Employee.set_raise(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_1.raise_amount)