# lambda for anon functions
# like def, but you don't assign it a name. It just returns the code
# Can assign it a name though if you want.
# Usually used for small chunks of code

sum_1 = lambda x, y : x + y

print("Sum :",sum_1(4,5))

can_vote = lambda age: True if age >= 18 else False

print("Can Vote :", can_vote(16))

power_list = [lambda x: x ** 2,
              lambda x: x ** 3,
              lambda x: x ** 4]

for func in power_list:
    print(func(4))

attack = {'quick': (lambda: print("quick attack")),
          'power': (lambda: print("power attack")),
          'miss': (lambda: print("The attack missed"))}

attack['quick']() #why do i need the ()????

import random



attack_key = random.choice(list(attack.keys()))
attack[attack_key]()

# problem
# create random list of heads or tails
# output number of heads or tails

acc = []
coin_flip = ['Heads','Tails']
for i in range(100):
    flip = random.choice(coin_flip)
    acc.append(flip)

print("Heads :",acc.count("Heads"))
print("Tails :",acc.count("Tails"))

# MAP!!!!!
# Execute a function on each item in a list

one_to_ten = range(1,11)

def double_it(num):
    return num * 2

print(type(list(one_to_ten)))
print(list(map(double_it, one_to_ten)))
print("-----")
new_list = list(one_to_ten)
print(list(map(double_it, new_list)))
print("-----")
print(list(map((lambda x: x * 3),one_to_ten)))
print("-----")
print(list(map((lambda x, y : x + y),[1,2,3],[4,5,6])))

# filtering lists with lambdas

print(list(filter((lambda x: x % 2 == 0), range(1,11))))