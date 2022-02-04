import sys
from collections import Counter

# 1) Iterate with enumerate() instead of range len()
data = [1, 2, -4, -3]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)

# 2) Use list comprehension instead of raw of for loops
squares = [i*i for i in range(10)]
print(squares)

# 3) Sort complex iterables with sorted()
data = [2, 0, 9, 3, 15, 4, -5]
# sorted_data = sorted(data)
sorted_data = sorted(data, reverse=True)
print(sorted_data)

data = [{'name':"Dicken", "age":26},
        {'name':"Davy", "age":29},
        {'name':"Dimitch", "age":22},
        {'name':"Blanchard", "age":24}]

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)


# 4) Store unique value with Sets
my_list = [1, 2, 3, 5, 6, 6, 7, 8, 8, 7, 7, 9, 9, 0]
my_set = set(my_list)
print(my_set)

# 5) Save memories with Generators
my_list = [i for i in range(1000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(1000))
print(sum(my_gen))
print(sys.getsizeof(my_gen), "bytes")

# 6) Define default values in Dictionaries with .get() and .setdefault()
my_dict = {"item":"football", "price":10.00}
count = my_dict.get('count', 0)
print(count)

count = my_dict.setdefault('count', 0)
print(my_dict)


# 7) Count hashable objects with collections.Counter

my_list = [10, 10, 10, 3, 4, 4, 4, 5, 6, 6, 3, 3, 8, 8, 2]
counter = Counter(my_list)
print(counter)
print(counter[10])
most_common = counter.most_common()
print(most_common[0])

# 8) Format a string
name = "Rolvy"
my_string = f"Hello {name}"
print(my_string)

# 9) Concat string with .join()
list_of_strings = ["Hello", "my", "friend"]
my_string = " ".join(list_of_strings)
print(my_string)


# 10) Merge two dictionaries 
d1 = {"name":"Dicken", "Age":26}
d2 = {"name":"Dicken", "city":"Paris"}
merged_dict = {**d1, **d2}
print(merged_dict)


# 11) Simplify if statement for multiple checks
colors = ['red', 'green', 'blue']
c = 'red'
if c in colors:
    print(f'{c} is in colors.')