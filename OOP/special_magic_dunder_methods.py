
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

        
        

emp_1 = Employee('Dicken', 'NGOLO', 5000)
emp_2 = Employee('Dimitch', 'MOUKEBA', 6500)


print(repr(emp_1))
print(emp_1.__str__())
