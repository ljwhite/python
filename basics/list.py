import random

rand_list = ["string", 1.234, 26]
one_to_ten = list(range(11))
rand_list = rand_list + one_to_ten
print(rand_list)
print("list length :",len(rand_list))
first_3 = rand_list[0:3]
print("first three :", first_3)
for i in first_3:
    print("{} : {}".format(first_3.index(i),i))

print((first_3[0] + " ") * 3)
print("index of 'string' :", first_3.index("string"))
first_3[0] = "new string"
print(first_3[0])
first_3.append("last string")
print(first_3[-1])

# problem

num_list = []
for i in range(5):
    i = random.randrange(1,9)
    num_list.append(i)

print("--------")
print("Here's the list!",num_list)

# bubble sort
i = len(num_list) - 1
while i > 1:
    j = 0
    k = 1
    x = 1
    while j < i:
        print("~~>~~>~~>")
        print("Iteration {}. Is {} > {}?".format(k, num_list[j], num_list[j+1]))

        if num_list[j] > num_list[j+1]:
            print("Yes. So we need to switch.")
            temp = num_list[j]
            num_list[j] = num_list[j+1]
            num_list[j+1] = temp
        else:
            print("Nope! Leave as is.")
        j += 1
        # for k in num_list:
        #     print(k, end="")
        print(num_list)
        k += 1
    print("End of Round")
    print("----------")
    i -= 1

num_list = []
for i in range(5):
    num_list.append(random.randrange(1,9))

num_list.sort()
num_list.reverse()
print(num_list)
num_list.insert(5,10)
print(num_list)
num_list.remove(10)
print(num_list)
num_list.pop(2)
print(num_list)

for k in num_list:
    print(k, end=", ")
