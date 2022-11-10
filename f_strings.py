name = 'Eric'
age = 74

print("Hello, {1}. You are {0}.".format(age, name))

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(**person))
print("Hello, {name}. You are {age}.".format(name=person['name'], age=person['age']))

### f-string
print(f"Hello, {name}. You are {age}.")
print(F"Hello, {name}. You are {age}.")

### Arbitrary expressions
a = f"{2 * 37}"
print(a)

def to_lowercase(input):
    return input.lower()

name = 'Rolvy Dicken'
print(f'{to_lowercase(name)} is interesting.')

name = 'Dicken'
print(f'{name.lower()} is interesting.')


class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name 
        self.last_name = last_name 
        self.age = age 

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name} is {self.age}."
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"

new_comedian = Comedian("Dicken", "NGOLO", 25)
print(f"{new_comedian}")
