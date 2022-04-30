####### ---- from 'https://realpython.com/primer-on-python-decorators/'

####--- Functions as First class Objects

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))
print('\n')


####--- Inner Functions
def parent():
    print('Printing from the parent() function')

    def first_child():
        print('Printing from the first_child() function')

    def second_child():
        print('Printing from the second_child() function')

    second_child()
    first_child()

# print(parent())


####--- Returning Functions from Functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num==1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(first())
print(second())

################################ 
####---  Simple Decorators  ####
################################

####--- First example

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening fater the function is called")
    return wrapper


def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
print(say_whee)


@my_decorator
def say_whee():
    print("Whee!")

print(say_whee())

####--- Second example
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7<= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper

def say_haha():
    print("Haha!")

say_haha = not_during_the_night(say_haha)
print(datetime.now())
print(say_haha())


####--- Decorating functions with arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_hello(name):
    print(f"Hello {name}. You look awesome.")

print(say_hello("Dicken"))

####--- Returning Values From Decorated Functions
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting.")
    return f"Hi {name}"

greeting = return_greeting("Dicken")
print(greeting)

#Check decorated function attributes
print("\nBefore using functools")
print(return_greeting)
print(return_greeting.__name__)
print(help(return_greeting))


#Check decorated function attributes again
import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting.")
    return f"Hi {name}"

# greeting = return_greeting("Dicken")
# print(greeting)

#Check decorated function attributes
print("\nAfter using functools")
print(return_greeting)
print(return_greeting.__name__)
print(help(return_greeting))
