
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

    @classmethod
    def set_araise_amt(cls, amount):
        cls.raise_amt = amount   

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


emp_1 = Employee('Dicken', 'NGOLO', 5000)
emp_2 = Employee('Dimitch', 'MOUKEBA', 6500)


import datetime

my_date = datetime.date(2022, 4, 24)
print(Employee.is_workday(my_date))