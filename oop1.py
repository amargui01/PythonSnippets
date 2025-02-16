class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return  f'{self.first} {self.last}'


emp_1 = Employee('youss', 'amar', 50000)
emp_2 = Employee('Joe', 'rama', 60000)

print(emp_1.fullname())
print(emp_2.fullname())