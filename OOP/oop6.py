class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    # allow to use fullname() as a variable fullname
    @property
    def fullname(self):
        return  f'{self.first} {self.last}'

    # allow to use email() as a variable email
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    # allow to create instance variable by passing a string this method
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # allow to delete by setting instance variables to None
    @fullname.deleter
    def fullname_del(self):
        print('Deleted Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Youss', 'Amar')

emp_1.fullname = 'John smith'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname_del
