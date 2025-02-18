class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    # return employee full name
    def fullname(self):
        return  f'{self.first} {self.last}'
    # replicate dunder allow to replicate the instance once passed to print()
    def __repr__(self):
        return f'Employee({self.first},{self.last},{self.pay})'
    # return fullname---> email
    def __str__(self):
        return f'{self.fullname()}--->{self.email}'
    # add the emp_1 and emp_salary
    def __add__(self, other):
        return self.pay + other.pay
    # return the length of fullname
    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('youss', 'amar', 50000)
emp_2 = Employee('Joe', 'rama', 60000)

# when repr and str both exist the value of repr is returned
print(emp_1)
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

# print(emp_1 + emp_2)
print(len(emp_1))
