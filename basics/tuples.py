my_tuple = (1,2,3,5,8)
print("1st value :",my_tuple[0])
print("1st 3 values :",my_tuple[0:3])
print("Length :", len(my_tuple))
more_fibs = my_tuple + (13,21,34)
print("34 in tuple? :", 34 in more_fibs)

for i in more_fibs:
    print(i)

a_list = [55,89,144]
a_tuple = tuple(a_list)
b_list = list(a_tuple)
print("Max :", max(a_tuple))
print("Min :", min(a_tuple))
