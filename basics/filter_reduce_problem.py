# problem

# find multiples of nine of random 100 value list containing values between 1-1000
import random
from functools import reduce

generated_list = list(random.randrange(1,1001) for i in range(100))

# for i in range(100):
#     i = random.randrange(1,1001)
#     generated_list.append(i)

print(generated_list)
filtered_list = list(filter((lambda x: x % 9 == 0), generated_list))
print(filtered_list)

print(reduce((lambda x, y: x+y),range(1,6)))

# problem 1
# create a list from 1 to 10
# function dbl_num
# map to generate a list that uses function on the list
# or just use a lambda

generated_list = list(i for i in range(1,11))

doubled_list = list(map((lambda x: x * 2), generated_list))
print(doubled_list)

# problem 2
# use filter with lambda to print out even values from 1-10 in a list
generated_list = list(i for i in range(1,11))
print(list(filter((lambda x: x % 2 == 0),generated_list)))

# problem 3
# use reduce with lambda to add up values 1-5
generated_list = list(i for i in range(1,6))
print(reduce((lambda x, y: x+y),generated_list))
#remember, end result of reduce is NOT a list