class Employee:

    raise_amount = 1.04
    num_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_employees += 1

    def fullname(self):
        full_name = f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)



emp_1 = Employee('youss', 'amar', 50000)
emp_2 = Employee('Joe', 'rama', 60000)

# writable attributes of instance
print(emp_1.__dict__)
# writable attributes of class
print(Employee.__dict__)
emp_1.apply_raise()
# employee one after the raise
print(emp_1.pay)

# num of employees
print(Employee.num_employees)

