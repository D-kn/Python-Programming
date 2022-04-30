import os
from zipfile import ZipFile
import zipfile


#### KeyError  ####

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
print(f'{person} is {ages[person]} years old.')

zip_file = ZipFile('zip_file.zip')
info = zip_file.getinfo('incomes.xlsx')
print(info)


##################################
### Handle a python KeyError  ####
##################################

#### .get()
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
age = ages.get(person)
if age:
    print(f'{person} is {age} years old.')
else:
    print(f'{person}\'s age is unkown.')

person = input('Get age for: ')
age = ages.get(person)
if age:
    print(f'{person} is {age} years old.')
else:
    print(f'{person}\'s age is unkown.')

person = input('Get age for: ')
age = ages.get(person, 0) #if KeyError return 0 (the default value)
print(f'{person} is {age} years old.')

#### try except
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
try:
    print(f'{person} is {ages[person]} years old.')
except KeyError:
    print(f'{person}\'s age is unkown.')
