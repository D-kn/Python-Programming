import sys

##############
#  Exception #
##############

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

#----- Assert
assert('linux' in sys.platform), "this code only works on Linux only."


#----- try and except block

def linux_interaction():
    assert('linux' in sys.platform), "Function can only run on linux systems."
    # print('Doing something.')

try:
    linux_interaction()
except: # excude this code when there is an exception                                    
    print('Linux function wasn\'t executed.')

try:
    linux_interaction()
except AssertionError as error: # excude this code when there is an exception                                    
    print(error)
    print('The linux_interaction() function was not executed.')


# #### KeyError  ####

ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
print(f'{person} is {ages[person]} years old.')



# ###################################
# #### Handle a python KeyError  ####
# ###################################

#----- .get()
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

#----- try except
ages = {'Jim': 30, 'Pam': 28, 'Kevin': 33}
person = input('Get age for: ')
try:
    print(f'{person} is {ages[person]} years old.')
except KeyError:
    print(f'{person}\'s age is unkown.')

