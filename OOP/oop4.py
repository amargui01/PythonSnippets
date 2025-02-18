# class inheritance
class Employee:

    raise_amount = 1.04
    num_employees = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_employees += 1
    # return fullname
    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        # use super() to inherit class variales
        super().__init__(first, last, pay)
        # intialize the pro_lang within Developer class
        self.prog_lang = prog_lang

class Manager(Employee):
    # set employee to None as a default
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        # if no list is passed create employees list
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    # add emp to employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    # remove emp from employees
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print(f'--->{emp.fullname()}')

# create 2 developers
dev_1 = Developer('amine', 'Reh', 50000,'python')
dev_2 = Developer('Foo', 'Gama', 60000, 'java')

# create 2 manager and pass to each a developer in a list
mgr_1 = Manager('Soo', 'Rana', 90000,[dev_1])
mgr_2 = Manager('Foo', 'Dama', 80000, [dev_2])

# add dev_2 to mgr_1
mgr_1.add_emp(dev_2)
# print employees mgr_1 manage
mgr_1.print_emps()
# remove dev_2 from the list mgr_1 manage
mgr_1.remove_emp(dev_2)
# print list of employees mgr_1 manage
mgr_1.print_emps()
# print num of employees
print(Employee.num_employees)
print(dev_1.email)
print(dev_1.prog_lang)
# lookinto the details of the developer instance
print(help(Developer))
# print(dev_1.email)
print(dev_2.email)

print(dev_1.pay)
# set the raise inside the Developer instance
dev_1.apply_raise()
print(dev_1.pay)

# mgr_1 is instance of Manager
print(isinstance(mgr_1,Manager))
# mgr_1 is instance of Developer
print(isinstance(mgr_1,Developer))