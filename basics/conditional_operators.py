drink = input("coke or pepsi : ")
if drink == "Coke":
    print("here is your coke")
elif drink == "Pepsi":
    print("here is your pepsi")
else:
    print("here is your water")

num_1, operator, num_2 = input("Enter Calculation : ").split()
num_1 = int(num_1)
num_2 = int(num_2)

if operator == "+":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 + num_2))
elif operator == "-":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 - num_2))
elif operator == "*":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 * num_2))
elif operator == "/":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 / num_2))
elif operator == "%":
    print("{} {} {} = {}".format(num_1, operator, num_2, num_1 % num_2))
else:
    print("womp womp")

age = int(input("Enter Age : "))
if (age >= 1) and (age <= 18):
    print('important birthday')
elif (age == 21) or (age == 50):
    print('importnat birthday')
elif not age < 65:
    print("Important Birthday")
else:
    print("not important")

age = int(input("Enter Age : "))
if age == 5:
    print("kingergarden")
elif age < 5:
    print("too young for school")
elif (age > 5) and (age <= 17):
    print("Go to Grade {}".format(age - 5))
elif age > 17:
    print("go to college")
else:
    print('no school for you')

# ternary operator condition if true or false
age = int(input("Enter Age : "))
can_vote = True if age >= 18 else False
print("You can vote :", can_vote)
