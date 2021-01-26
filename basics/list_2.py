# list comprehensions

import math

even_list = [(i + 1) for i in range(9)]
print(even_list)

num_list = [1,2,3,4,5]
list_of_values = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)] for m in num_list]
print(list_of_values)

mult_d_list = [[0]*10 for i in range(10)]
mult_d_list[0][1] = 10
print(mult_d_list)

for i in range(10):
    for j in range(10):
        mult_d_list[i][j] = "{} : {}".format(i,j)
#
# print(mult_d_list)
#
# for i in range(10):
#     for j in range(10):
#         print(mult_d_list[i][j], end=" || ")


problem_list = [[0]* 10 for i in range(10)]
print(problem_list)

for i in range(1,10):
    for j in range(1,10):
        problem_list[i][j] = i * j
        print(problem_list[i][j], end=", ")
    print()

print("-------")
print(problem_list)
print("-------")
for i in range(1,10):
    for j in range(1,10):
        print(problem_list[i][j],end=", ")
    print()
print("-------")
print(problem_list)

even_list = [i*2 for i in range(5)]
print(even_list)

even_list_alt = [i%2 for i in range(10)]
print(even_list_alt)