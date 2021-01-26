import random

for i in range(1,21):
    if i % 2 != 0:
        print(i)

your_float = float(input("Enter a float : "))
print("Rounded to 2 decimals : {:.2f}".format(your_float))

amount, interest = (input("Enter investment principal and interest : ")).split()
amount = float(amount)
interest = float(interest) * .01
for i in range(1,11):
    amount = amount * (1 + interest)
    # print("Amount in year {}: {}".format(i, amount))

print("Investment after 10 years : ${:.2f}".format(amount))

rand = random.randrange(1,51)
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    if i == 15:
        break
    print("Odd: ",i)
    i += 1

rows = int(input("Number of rows:"))
for i in range(1,rows+1):
    spaces = rows - i
    hashes = i * 2 - 1
    print(" "* spaces + "#" * hashes)
stump_spaces = rows - 1
print(" " * stump_spaces + "#")

spaces = rows - 1
hashes = 1
stump_spaces = rows - 1
while rows != 0:
    for i in range(spaces):
        print(' ', end="")
    for i in range(hashes):
        print("#", end="")
    print()
    spaces -= 1
    hashes += 2
    rows -= 1
for i in range(stump_spaces):
    print(" ", end="")
print("#")
