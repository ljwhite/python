# list comprehension - execute code against an iterable
# list comprehension syntax
# my_list = [ expression / for item in iterable / (if condition) ]
# 1) for loop
# 2) expression to deal with the item
# 3) if condition (optional

import random

print(list(map((lambda x: x * 2),range(1,11))))

#same thing, but with a list comprension:
print([2 * x for x in range(1,11)])

print(list(filter((lambda x: x % 2 != 0), range(1,11))))
#same thing
print([x for x in range(1,11) if x % 2 != 0])

# replace for loops
name = "Lito White"
name_list = []
for i in name:
    name_list.append(i)

print(name_list)

# After
name = "Sarah Aylward"
name_list = [x for x in name]
print(name_list)

# list comprehension works on any iterable. String is an iterable (or course)
# Replace lambda operators (same idea, cleaner code)

# consolidate nested loops
names = ["tim","doug","mike","anthony"]
name_list = [letter for name in names for letter in name]
print(name_list)

#ternary operators (if/else)
# NOTE THE SYNTAX CHANGE FOR TERNARY!! [expression / if / else / item in iterable]
names = ["tim","doug","mike","anthony"]
name_list = [name if len(name) >= 4 else "another name" for name in names ]
print(name_list)

# Replacement for higher functions (map, filter, count, etc)
# map(function, iterable)
# [expression / item in iterable]
# filter(condition, iterable)
# [ expression / item in iterable / if condition ] NOTE expression is logically just returning the item for filter

# generate list of 50 values (1 thru 50, square them, then filter for multiples of eight
generated_list = [i ** 2 for i in range(50) if i % 8 == 0]
print(generated_list)

# modify two different lists
# SYNTAX: [ expression(x,y) / for x / for y ]
generated_list = [x * y for x in range(1,3) for y in range(11,16)]
print(generated_list)

# list comprehension in list comprehension
# generate 10 values, multiply them by 2, return multiples of 8
# OVERVIEW: work inside out. Manipulate the list first, then filter manipulated list
generated_list = [i * 2 for i in range(10) if (i * 2) % 8 == 0]
print(generated_list)
generated_list = [ x for x in [i * 2 for i in range(10)] if x % 8 == 0]
print(generated_list)

# Problem
# generate list of 50 random values between 1-1000, return multiples of nine
# nested list comprehension
generated_list = [x for x in [random.randint(1,1001) for i in range(50)] if x % 9 == 0]
print(generated_list)

# multi dimensional lists
multi_list = [[1,2,3],
              [4,5,6],
              [7,8,9]]

print([col[1] for col in multi_list])

# print diagonals [1,5,9]
# target_list =  [multi_list[0][0], multi_list[1][1], multi_list[2][2]]
generated_list = [multi_list[i][i] for i in range(len(multi_list))]
print(generated_list)

# GENERATORS. Create results spread over time, don't need to create right away.

def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
        return True

def gen_prime(max_number):
    for num1 in range(2,max_number):
        if is_prime(num1):
            yield num1

prime = gen_prime(50)
print("Prime :", next(prime))
print("Prime :", next(prime))
print("Prime :", next(prime))

# Now make it a generator
double = (x * 2 for x in range(10))
print("Double :", next(double))
print("Double :", next(double))
print("Double :", next(double))
